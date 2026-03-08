---
title: "Спецификация: CDM v2 — LC->CF Mapping Profile"
date: 2026-03-06
tags: [CDM, v2, LC-6, CF-6, mapping, profile]
citekey: cdm_v2_lc_cf_mapping_profile_ru_2026
---

# Спецификация: CDM v2 — LC->CF Mapping Profile

> Документ задает минимальный профиль отображения LC-фазы в параметры исполнения
> CF-цикла в рамках переходного слоя CDM v2.

---

## 1. Область применения

Профиль определяет для каждой `LC`-фазы:

- бюджет ресурса цикла `R_phase`;
- допустимый риск необратимых затрат `tau_risk_max`;
- приоритеты `CF1..CF6`;
- минимальные критерии выхода `exit_criteria`.

Профиль является policy-dependent и может уточняться доменом.

---

## 2. Минимальный интерфейс

```yaml
lc_cf_profile:
  phase: F1|F2|F3|F4|F5|F6
  R_phase: low|medium|high
  tau_risk_max: low|medium|high
  priority:
    CF1: low|normal|high
    CF2: low|normal|high
    CF3: low|normal|high
    CF4: low|normal|high
    CF5: low|normal|high
    CF6: low|normal|high
  exit_criteria:
    ds_trend: increase|decrease|stable|unstable
    eval_window: integer
    additional: optional
```

---

## 3. Рекомендуемая таблица соответствия

| LC phase | R_phase | tau_risk_max | CF-priority focus | Minimal exit_criteria |
|---|---|---|---|---|
| F1 | medium | low | CF1, CF2, CF6 | exists=true, DS starts decreasing |
| F2 | high | medium | CF2, CF3, CF4 | DS decreases on >= tau_phase_min |
| F3 | medium | medium | CF3, CF4, CF6 | DS <= DS_stable and stable eval |
| F4 | high | low | CF1, CF2, CF6 | DS growth stabilized or reversed |
| F5 | low | low | CF6 | irreversible condition fixed and closure path chosen |
| F6 | low | low | CF6 | exists=false or Tag switched |

---

## 4. Нормативные правила

- `CF6` обязателен во всех LC-фазах как точка оценки и связи с LC.
- Изменение метрик `LC` допускается только через `CF6/Evaluate`
  (фазы `CF1..CF5` не изменяют `LC` напрямую).
- Для `F4/F5` запрещено повышать `tau_risk_max` выше policy-лимита родительской системы.
- Для `F1/F2` недопустимо опускать `CF1/CF2` ниже `normal`.
- Для `F5/F6` `CF5` не является обязательным: закрывающий цикл может идти через
  фиксацию результата/завершения.

Интерпретация `Psi: stats({CF6_k}) -> LC_phase` трактуется как
policy-dependent классификатор и не задается как универсальная биекция.

---

## 5. Интеграция с переходным слоем

Профиль реализует контракт `LC -> CF`, объявленный в:

- [[fcdm-core/theory/cdm/Specifications/CDM-v2-Transition-Spec|CDM-v2-Transition-Spec]]
- [[fcdm-core/theory/cdm/Specifications/CDM-v2-Minimality-Theorem|CDM-v2-Minimality-Theorem]]

Использование профиля не меняет канонические предикаты `LC` и порядок фаз `CF`.

Готовый шаблон:

- [[fcdm-core/theory/cdm/Specifications/templates/lc_cf_profile.yaml|lc_cf_profile.yaml]]
