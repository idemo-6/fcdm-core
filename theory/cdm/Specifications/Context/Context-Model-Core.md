---
title: "Модель: Context Core (междоменная)"
date: 2026-02-28
tags: [CDM, Context, model]
citekey: cdm_context_model_core_ru_2026
---

# Модель: Context Core (междоменная)

## 1. Назначение

Документ задает формальную междоменную модель контекста.

Это не канон терминов, а модель вычисления:
- `C_active`;
- `C_candidates`;
- `Applicable(Intent, C_active, LC_phase)`;
- выбора `OperatorSet`.

## 1.1 Принципы модели

Модель использует следующие канонические допущения:

1. `System-first`: объектом моделирования является единая система `Y`.
2. `Domain-as-context`: доменные описания интерпретируются как контексты `Ck` системы `Y`.
3. `Cross-context semantics`: согласование между `Ci` и `Cj` моделируется явно, а не как внешняя пост-обработка.

Формально:

`DomainView_k(Y) := Projection(Y, Ck)`.

Из этого следует, что разные доменные описания одной системы должны сравниваться и координироваться как межконтекстные проекции `Y`, а не как независимые системы.

---

## 2. Структура контекста

Базовая структура:

`C = <id, type, scope, constraints, resources, operators, priority, validity_interval>`.

Где:
- `constraints` — ограничения на состояния и переходы;
- `resources` — доступные ресурсы;
- `operators` — множество допустимых операторов;
- `priority` — приоритет в разрешении конфликтов;
- `validity_interval` — интервал применимости.

---

## 3. Активация контекста

Для системы `Y` и времени `t`:

`C_avail(Y, LC_phase) = Gate(C-Layer(Y), LC_phase, policy_Y)`.

`C_candidates(Y, t) = { C in C-Layer(Y) | Active(C, Y, t) = true }`.

Ограничение доступности:

`C_candidates(Y, t) subseteq C_avail(Y, LC_phase(t))`.

`C_active(Y, t) = SelectActive(C_candidates(Y, t), policy, branch_id)`.

Ограничение:

`C_active(Y, t) in C-Layer(Y)`.

В каждой исполнительной ветке (`branch_id`) в момент `t` активен ровно один контекст.

Минимальный предикат активности:

`Active(C, Y, t) := Valid(C, t) and Relevant(C, Y, t)`.

Для иерархии систем (`Parent -> Child`):

`policy_child <= policy_parent` и
`C_avail_child(LC_phase_child) subseteq C_avail_parent(LC_phase_parent, policy_parent)`.

---

## 4. Доступные операторы

`OperatorSet(C_active, LC_phase) = C_active.operators \ Forbidden(C_active, LC_phase)`.

`Forbidden(C_active, LC_phase)` определяется ограничениями текущего активного контекста и фазовыми ограничениями.

При межконтекстной задаче объединение операторов выполняется не в runtime одной ветки, а на уровне координации результатов переключений/веток.

---

## 5. Предикат применимости Intent

`Applicable(Intent, C_active, LC_phase) := exists pi_CF, pi_ops : Realize(Intent, LC_phase, pi_CF, pi_ops)`

при условиях:
- `pi_CF` совместим с `CF1..CF6`;
- `pi_ops subseteq OperatorSet(C_active, LC_phase)`;
- `pi_ops` не нарушает `constraints(C_active)` и ограничения `LC_phase`.

Следствия:
- `not Defined(Intent, C_active) => not Applicable(Intent, C_active, LC_phase)`;
- `Applicable(Intent, C_active, LC_phase) => Defined(Intent, C_active)`.

---

## 6. LC allowlist и declared/materialized валидация (ICSS profile)

Пусть:

- `DeclaredCtxSet` — контексты, объявленные в collect/declaration блоке;
- `MaterializedCtxSet` — контексты, реально материализованные через `pt.*`.

Тогда для LC-политики:

`DeclaredCtxSet subseteq allow.contexts_declared(LC_phase)` (если список задан),

`MaterializedCtxSet subseteq allow.contexts_used(LC_phase)` (если список задан; иначе используется `allow.contexts_declared`).

Базовый инвариант:

`MaterializedCtxSet subseteq DeclaredCtxSet`.

---

## 7. Семантика Experience=0 на Intent-уровне

На Intent-уровне:

`Experience = 0 <=> not Applicable(Intent, C_active, LC_phase)`.

Это включает частный случай неопределенности (`not Defined`), но не сводится к нему.

Декомпозиция неприменимости:

1. `Inapplicable_due_to_undefined`: `not Defined => not Applicable`.
2. `Inapplicable_despite_defined`: `Defined and not Applicable`.

---

## 8. Конфликты контекстов

Если для задачи требуется согласование нескольких контекстов (`|C_candidates| > 1`) и их ограничения конфликтуют:

1. применяется контекст с более высоким `priority`;
2. при равном `priority` применяется политика разрешения конфликтов домена;
3. если конфликт неразрешим, `Applicable = false` и возвращается `Experience = 0`.
