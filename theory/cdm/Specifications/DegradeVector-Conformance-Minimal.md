---
title: "Conformance: DegradeVector Minimal Tests"
date: 2026-03-05
tags: [CDM, DegradeVector, conformance, tests]
citekey: cdm_degradevector_conformance_minimal_ru_2026
---

# Conformance: DegradeVector Minimal Tests

## 1. Назначение

Документ задает минимальные conformance-проверки для `DegradeVector/DS`:
- диапазоны и направление шкалы;
- точка фиксации в `CF6`;
- разделение `runtime.result` и `analysis.op_signal`.

---

## 2. Тест-набор (минимум)

### T1: DS range

Вход:
- валидный `degrade_vector`.

Ожидание:
- `0 <= ds.value <= 1`.

### T2: Direction invariant

Вход:
- набор случаев с улучшением и деградацией.

Ожидание:
- лучшее состояние не может иметь большее значение `DS`, чем худшее;
- `direction == 0_best_1_worst`.

### T3: CF6-only update

Вход:
- попытка фиксации `DegradeVector/DS` при `cf_phase=CF3` и `cf_phase=CF6`.

Ожидание:
- `CF3` отклоняется;
- `CF6` допускается.

### T4: Result zero semantics

Вход:
- кейсы с `runtime.result=0`.

Ожидание:
- `result=0` допустим только при `ApplicabilityFailure`.

### T5: Analytics separation

Вход:
- кейсы с `analysis.op_signal=0`.

Ожидание:
- `op_signal=0` не трактуется как `runtime.result=0` автоматически;
- поля проверяются независимо.

### T6: Weight normalization

Вход:
- компоненты `rr_i` с весами.

Ожидание:
- `sum(weight_i)` в допустимом отклонении от `1`.

---

## 3. Минимальный формат отчета

```yaml
suite: "degradevector_minimal_v1"
entity_id: "sys:domain/name#hash8"
status: "pass|fail"
tests:
  - id: "T1"
    status: "pass|fail"
    details: ""
  - id: "T2"
    status: "pass|fail"
    details: ""
  - id: "T3"
    status: "pass|fail"
    details: ""
  - id: "T4"
    status: "pass|fail"
    details: ""
  - id: "T5"
    status: "pass|fail"
    details: ""
  - id: "T6"
    status: "pass|fail"
    details: ""
```
