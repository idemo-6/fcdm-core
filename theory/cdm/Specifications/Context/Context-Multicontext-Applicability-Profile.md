---
title: "Профиль: Multicontext Applicability (прикладной)"
date: 2026-03-01
tags: [CDM, Context, CtxL, profile, multicontext, applicability]
citekey: cdm_context_multicontext_applicability_profile_ru_2026
---

# Профиль: Multicontext Applicability (прикладной)

## 1. Назначение

Документ задает прикладные правила, как учитывать межконтекстные взаимодействия
в одной системе `Y` при оценке `Defined/Applicable/Result`.

Профиль не переопределяет канон, а фиксирует операционные требования для
воспроизводимого применения в runtime и domain-профилях.

---

## 2. Нормативные ссылки

- `Context-Canonical.md`
- `Context-Model-Core.md`
- `Context-Coordination-Protocol.md`
- `Context-Coordination-Policy-Default.md`
- `../CtxL/CtxL-Canonical.md`

---

## 3. Базовые правила профиля

1. `System-first`:
- все доменные представления относятся к одной системе `Y`.

2. `Domain-as-context`:
- доменная модель трактуется как контекстная проекция `Y`, а не как отдельная система.

3. `Cross-context mandatory`:
- при `|C_candidates| >= 2` межконтекстное влияние должно быть явно учтено
  через матрицу влияний или через эквивалентный формальный механизм.

4. `Non-collapse`:
- `Undefined` и `Inapplicable` не сливаются;
- `Undefined` учитывается как частный случай неприменимости.

---

## 4. Матрица межконтекстного влияния (минимум)

Для каждого домена задается матрица:

`ImpactMatrix[Ci -> Cj] = <strength, lag, condition, confidence>`.

Где:
- `strength in [0,1]` — сила влияния;
- `lag` — задержка влияния;
- `condition` — условие активации влияния;
- `confidence in [0,1]` — доверие к оценке.

Минимальное требование:
- для каждого активного `Ci` должны быть определены все критичные `Ci -> Cj`
  переходы, влияющие на `Applicable` и/или `Result`.

---

## 5. Applicability Guards (runtime)

Перед фиксацией исполнимого решения:

1. Проверить `Defined(Intent, C_active)`.
2. Проверить `Applicable(Intent, C_active, LC_phase)`.
3. Применить межконтекстные guard-проверки по `ImpactMatrix`.

Если решение валидно в одном контексте, но нарушает constraints более
приоритетного контекста, решение запрещается и возвращается `Result=0`.

---

## 6. Эскалация межконтекстного конфликта

Эскалация в `C_coord/C_meta` обязательна, если:

1. обнаружена дивергенция между контекстами с пересечением критичных ограничений;
2. `confidence` трансляции ниже `tau_translate`;
3. невозможно доказать безопасный `Aligned`-выход.

Допустимые выходы:
- `Aligned`,
- `Forked`,
- `Blocked`.

---

## 7. Контракт Result=0 (обязательная детализация)

При `Result=0` обязательно фиксировать:

1. `zero_class in {AF_sem, AF_epi, AF_sto, mixed}`;
2. `source_context` (контекст, в котором сформирована неприменимость);
3. `affected_contexts` (какие контексты блокируются/ограничиваются);
4. `reason_trace_ref` (ссылка на трассу решения).

Это устраняет смешение:
- неопределенности,
- неприменимости,
- межконтекстного конфликтного блокирования.

---

## 8. Re-evaluation Trigger Policy

После значимого изменения в контексте `Ci` должно выполняться:

`ReevalSet = { Cj | ImpactMatrix[Ci -> Cj].strength >= theta }`.

Для каждого `Cj in ReevalSet` повторно вычисляются:
- `Defined`,
- `Applicable`,
- прогноз `Result`.

Это правило обязательно для систем с высокой межконтекстной связностью
(человек, организация, socio-technical системы).

---

## 9. Минимальный YAML-контракт профиля

```yaml
multicontext_applicability_profile:
  system_id: "<Y>"
  thresholds:
    impact_strength_theta: 0.40
    translate_conf_tau: 0.70
  impact_matrix:
    - from: C_cog
      to: C_bio
      strength: 0.75
      lag: "P1D"
      condition: "stress_index > 0.6"
      confidence: 0.80
  result_zero_contract:
    require_zero_class: true
    require_source_context: true
    require_affected_contexts: true
    require_reason_trace_ref: true
  escalation:
    force_cbp_on_conflict: true
```

---

## 10. Статус

Профиль рекомендован как default-прикладной стандарт для мультиконтекстных
задач до появления доменно-специфического override.
