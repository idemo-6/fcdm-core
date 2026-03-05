---
title: "Контракт: DegradeVector Machine Contract (YAML/JSON)"
date: 2026-03-05
tags: [CDM, DegradeVector, DegradeScore, machine-contract, schema]
citekey: cdm_degradevector_machine_contract_ru_2026
---

# Контракт: DegradeVector Machine Contract (YAML/JSON)

## 1. Назначение

Документ задает минимальный машинный контракт для представления:
- `DegradeVector`;
- `DegradeScore (DS)`;
- аналитического сигнала `op_signal`.

Контракт не меняет каноническую семантику `Result`.

---

## 2. YAML-шаблон объекта

```yaml
entity_id: "sys:domain/name#hash8"
ts: "2026-03-05T10:00:00Z"
lc_phase: "F3"
cf_phase: "CF6"

degrade_vector:
  components:
    - id: "rr_reliability"
      value: 0.22
      weight: 0.35
      source: "https://example.org/datasets/reliability_v1.csv"
    - id: "rr_cost"
      value: 0.48
      weight: 0.25
      source: "https://example.org/datasets/cost_v2.csv"
    - id: "rr_latency"
      value: 0.31
      weight: 0.40
      source: "https://example.org/datasets/latency_v3.csv"

  agg:
    function_id: "weighted_sum_sigma_v1"
    params:
      sigma: "identity"

ds:
  value: 0.33
  direction: "0_best_1_worst"
  stable_threshold: 0.20
  warning_threshold: 0.35

analysis:
  op_signal: 1   # -1 | 0 | +1
  expected_delta_ds_sign: "negative"   # negative | zero | positive

runtime:
  result: 1      # +1 | 0 | -1
  result_zero_only_for: "ApplicabilityFailure"
```

---

## 3. JSON Schema (минимум)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "CDM DegradeVector Contract v1",
  "type": "object",
  "required": ["entity_id", "ts", "lc_phase", "cf_phase", "degrade_vector", "ds", "analysis", "runtime"],
  "properties": {
    "entity_id": { "type": "string", "minLength": 1 },
    "ts": { "type": "string", "format": "date-time" },
    "lc_phase": { "type": "string", "pattern": "^F[1-6]$" },
    "cf_phase": { "type": "string", "pattern": "^CF[1-6]$" },
    "degrade_vector": {
      "type": "object",
      "required": ["components", "agg"],
      "properties": {
        "components": {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "object",
            "required": ["id", "value", "weight"],
            "properties": {
              "id": { "type": "string", "minLength": 1 },
              "value": { "type": "number", "minimum": 0, "maximum": 1 },
              "weight": { "type": "number", "minimum": 0, "maximum": 1 },
              "source": { "type": "string" }
            }
          }
        },
        "agg": {
          "type": "object",
          "required": ["function_id"],
          "properties": {
            "function_id": { "type": "string", "minLength": 1 },
            "params": { "type": "object" }
          }
        }
      }
    },
    "ds": {
      "type": "object",
      "required": ["value", "direction"],
      "properties": {
        "value": { "type": "number", "minimum": 0, "maximum": 1 },
        "direction": { "const": "0_best_1_worst" },
        "stable_threshold": { "type": "number", "minimum": 0, "maximum": 1 },
        "warning_threshold": { "type": "number", "minimum": 0, "maximum": 1 }
      }
    },
    "analysis": {
      "type": "object",
      "required": ["op_signal"],
      "properties": {
        "op_signal": { "type": "integer", "enum": [-1, 0, 1] },
        "expected_delta_ds_sign": { "type": "string", "enum": ["negative", "zero", "positive"] }
      }
    },
    "runtime": {
      "type": "object",
      "required": ["result", "result_zero_only_for"],
      "properties": {
        "result": { "type": "integer", "enum": [-1, 0, 1] },
        "result_zero_only_for": { "const": "ApplicabilityFailure" }
      }
    }
  }
}
```

---

## 4. Семантические правила (поверх schema)

1. `cf_phase` для фиксации `DegradeVector/DS` должен быть `CF6`.
2. `sum(weight_i)` рекомендуется нормировать к `1` (допуск `+-1e-6`).
3. `ds.direction` всегда `0_best_1_worst`.
4. `runtime.result=0` допустим только при `ApplicabilityFailure`.
5. `analysis.op_signal` не используется как runtime-результат.
