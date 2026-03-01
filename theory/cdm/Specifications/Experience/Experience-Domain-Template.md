---
title: "Шаблон: Domain Experience Specification"
date: 2026-02-28
tags: [CDM, Experience, domain, template]
---

# Шаблон: Domain Experience Specification

## 1. Domain

- Domain ID:
- Domain Name:
- Связанный DomainLexicon:

---

## 2. Наблюдатель и локальность

- Кто является локальным наблюдателем:
- Где хранится `G_local`:
- Как актуализируется `G_cons`:

---

## 3. Структура Experience Graph

- Типы узлов:
- Типы причинных ребер:
- Весовые параметры:
- Политика архивирования/ослабления:

---

## 4. UpdateExp в CF6

Определить:
- входы `UpdateExp`;
- правила обновления для `+1/0/-1`;
- как фиксируется `zero_class`;
- `zero_structural_rule` (когда `Result=0` классифицируется как `0_structural`);
- `zero_epistemic_stochastic_rule` (когда `Result=0` классифицируется как `0_epistemic_stochastic`);
- как учитывается `LC_phase`.

---

## 5. Связь с DS/DegradeVector

Определить:
- функцию `Delta_DS = f_exp(...)`;
- наличие `epsilon_drift`;
- пороги/ограничения домена.

---

## 6. Операционный и аналитический уровни

Определить:
- runtime-хранимые поля;
- аналитические поля (`0_structural`, `0_epistemic_stochastic`, а также `AF_sem/AF_epi/AF_sto/mixed` при детализации);
- правила ретроспективного анализа.

---

## 7. Тесты валидации

- T1: фиксация опыта только в `CF6`;
- T2: корректная тринарность `Result`;
- T3: причинная прослеживаемость `Intent -> Context -> Operators -> Result`;
- T4: корректная обработка `Result=0`;
- T5: совместимость с `Applicable(Intent, C_active, LC_phase)`.
