---
title: "Спецификация: CDM v2 — Minimal Conformance Checklist"
date: 2026-03-06
tags: [CDM, v2, conformance, checklist, LC-6, CF-6]
citekey: cdm_v2_minimal_conformance_checklist_ru_2026
---

# Спецификация: CDM v2 — Minimal Conformance Checklist

> Документ фиксирует минимальные требования соответствия для внедрения CDM v2
> без полной доменной формализации.

---

## 1. Обязательные проверки

### C1. Полнота функциональных классов CF

Должны быть явно реализованы или проверяемо неявно присутствовать:

`collect, analyze, forecast, decide, implement, evaluate`.

### C2. Связь CF -> LC

Изменение метрик `LC` допускается только через `CF6` (Evaluate bridge).

### C2b. Applicability PT-gating

Должен быть реализован фазовый переход `PT(CF4->CF5)` с проверкой
`Applicable(Intent, C_active, LC_phase)`.

Обязательные ветки:

- `Applicable=true` -> переход в `CF5`;
- `Applicable=false` -> `PT(CF4->CF6:inapplicable)` с фиксацией `Result=0`.

### C3. LC->CF профиль

Для каждой активной `LC`-фазы должен быть задан `lc_cf_profile`:

- `R_phase`
- `tau_risk_max`
- `priority(CF1..CF6)`
- `exit_criteria`

### C4. Инвариант редукции неопределенности

На интервале наблюдения должно выполняться:

`E[Omega_after - Omega_before] <= 0`.

### C5. Метрика необратимой стоимости

Должна быть определена и логироваться метрика:

`E[tau_future]` (или ее валидный доменный аналог).

### C6. Интерпретационный профиль фаз

Должен быть описан `Psi: stats({CF6_k}) -> LC_phase` с policy-ограничениями.
`Psi` не должен декларироваться как универсальная биекция/изоморфизм.

---

## 2. Минимальные артефакты для аудита

- журнал фаз `CF1..CF6` (с меткой цикла);
- журнал `CF6`-результатов и изменений `LC`;
- журнал `PT(CF4->CF5)` с исходами `Applicable=true/false`;
- журнал веток `PT(CF4->CF6:inapplicable)` и фиксаций `Result=0`;
- декларация `lc_cf_profile` для используемых `LC`-фаз;
- описание метрик `Omega`-редукции и `tau`;
- описание `Psi`-правил.

---

## 3. Критерии статуса соответствия

- **Pass**: все проверки `C1..C6` + `C2b` выполнены.
- **Conditional Pass**: выполнены `C1..C3` + `C2b`, а `C4..C6` задекларированы с планом закрытия.
- **Fail**: нарушена хотя бы одна из `C1..C3` или `C2b`.

---

## 4. Совместимость

Чеклист является минимальным и совместим с:

- [[fcdm-core/theory/cdm/Specifications/CDM-v2-Transition-Spec|CDM-v2-Transition-Spec]]
- [[fcdm-core/theory/cdm/Specifications/CDM-v2-LC-CF-Mapping-Profile|CDM-v2-LC-CF-Mapping-Profile]]
- [[fcdm-core/theory/cdm/Specifications/CDM-v2-Minimality-Canonical-Short|CDM-v2-Minimality-Canonical-Short]]
