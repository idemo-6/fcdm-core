---
title: "Шаблон: Domain Context Specification"
date: 2026-02-28
tags: [CDM, Context, domain, template]
---

# Шаблон: Domain Context Specification

## 1. Domain

- System `Y` (единая система):
- Domain ID:
- Domain Name:
- Связанный DomainLexicon:

---

## 2. Mapping к канону Context

- `Context` в домене:
- `C-Layer` в домене:
- `C_active` в домене:
- Обоснование `Domain-as-context` (почему это контекстная проекция `Y`, а не отдельная система):

Указать соответствие каноническим определениям из `Context-Canonical.md`.

---

## 3. Типы контекстов домена

Для каждого типа:
- `type`:
- описание:
- типичные `constraints`:
- типичные `resources`:
- `operators`:
- базовый `priority`:

---

## 4. Правило активации

Определить `Active(C, Y, t)` в терминах наблюдаемых метрик домена.

Минимум:
- входные сигналы;
- пороги;
- интервал валидности.

---

## 5. OperatorSet домена

Определить:
- как строится `OperatorSet(C_active, LC_phase)`;
- какие операторы запрещаются;
- как применяются фазовые ограничения `LifeCycle`.

---

## 6. Applicable(Intent, C_active, LC_phase)

Определить проверяемые критерии:
- когда `Defined = true/false`;
- когда `Applicable = true/false`;
- что именно означает `Experience = 0` для домена.

---

## 7. Тесты валидации

- T0: `System-first` выполнен (домен описывает одну и ту же систему `Y`);
- T1: внешность контекста относительно `Y`;
- T2: наблюдаемое влияние на траектории `CF1..CF6`;
- T3: воспроизводимость вычисления `C_active`;
- T4: воспроизводимость вычисления `Applicable`;
- T5: согласованность `Experience=0` с `not Applicable`.
