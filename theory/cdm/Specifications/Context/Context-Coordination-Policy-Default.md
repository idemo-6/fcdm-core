---
title: "Политика: Context Coordination Protocol (default)"
date: 2026-02-28
tags: [CDM, Context, CDL, policy, default]
citekey: cdm_context_coordination_policy_default_ru_2026
---

# Политика: Context Coordination Protocol (default)

## 1. Назначение

Документ задает базовую (default) политику для `Context-Coordination-Protocol.md`:
- значения порогов;
- веса дивергенции;
- приоритеты типов контекстов;
- правила принятия решения.

Политика междоменная и может переопределяться доменным профилем.

---

## 2. Пороги по умолчанию

- `tau_translate = 0.70`
- `tau_soft = 0.25`
- `tau_hard = 0.60`

Интерпретация:
- `Div <= 0.25` -> мягкая дивергенция;
- `0.25 < Div <= 0.60` -> жесткая дивергенция;
- `Div > 0.60` -> критическая несовместимость.

---

## 3. Веса дивергенции по умолчанию

`Div = w_truth*d_truth + w_goal*d_goal + w_constraint*d_constraint + w_operator*d_operator`

Default:
- `w_truth = 0.20`
- `w_goal = 0.20`
- `w_constraint = 0.35`
- `w_operator = 0.25`

`sum(w_*) = 1.00`.

---

## 4. Приоритеты контекстов (default order)

Порядок (высокий -> низкий):

1. `C_phys`, `C_causal`
2. `C_meta`
3. `C_coord`
4. `C_legal`
5. `C_eco`
6. `C_org`
7. `C_info`
8. `C_noise`, `C_obs`

Примечание:
- домен может добавить/изменить типы контекстов;
- при доменном override должен сохраняться принцип невозрастания физико-каузальной допустимости.

---

## 5. Правила выбора выхода

1. Если `Applicable=false` хотя бы в одном критичном контексте -> `Blocked`.
2. Если `Conf < tau_translate` и нет валидного `C_coord`/`C_meta` -> `Blocked`.
3. Если `Div <= tau_soft` -> `Aligned`.
4. Если `tau_soft < Div <= tau_hard`:
- при успешном применении `R1..R4` -> `Aligned`;
- иначе -> `Forked`.
5. Если `Div > tau_hard`:
- при наличии устойчивой трансляции через `C_coord` при активной политике `C_meta` -> `Forked`;
- иначе -> `Blocked`.

---

## 6. Default классификация Result=0

При `Result=0` в `evaluate` применять порядок:

1. `AF_sem`: проверка принадлежности `SemanticSpace(C_active)`;
2. `AF_epi`: проверка полноты данных;
3. `AF_sto`: проверка стохастической разрешимости;
4. если срабатывает более одного условия -> `mixed`.

---

## 7. Формат policy-профиля (YAML)

```yaml
context_coordination_policy:
  thresholds:
    tau_translate: 0.70
    tau_soft: 0.25
    tau_hard: 0.60
  divergence_weights:
    w_truth: 0.20
    w_goal: 0.20
    w_constraint: 0.35
    w_operator: 0.25
  priorities:
    - C_phys
    - C_causal
    - C_meta
    - C_coord
    - C_legal
    - C_eco
    - C_org
    - C_info
    - C_noise
    - C_obs
  classify_zero_order:
    - AF_sem
    - AF_epi
    - AF_sto
```

---

## 8. Правило переопределения доменом

Доменный профиль может менять пороги, веса и приоритеты при условиях:

1. сохранена совместимость с `Context-Coordination-Protocol.md`;
2. физико-каузальные ограничения не понижаются ниже любого другого типа;
3. все изменения явно документированы в `Context-Domain-*.md`.
