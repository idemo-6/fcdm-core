---
title: "Examples: Canonical Versioning (document, deal, software)"
date: 2026-03-01
tags: [CDM, versioning, examples, document, deal, software]
citekey: cdm_versioning_examples_ru_2026
---

# Examples: Canonical Versioning

Нормативная база:

- [[fcdm-core/theory/cdm/Specifications/Versioning/Versioning-Canonical|Versioning-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/Versioning/Version-Derivation-Policy|Version-Derivation-Policy]]

---

## 1. Документ

Сущность:

- `EntityId = doc:core/doc-lifecycle#A17F9C2B`

Состояние:

- инкарнация: `1`
- LC: `F3` (`lc=3`)
- CF: `7`
- CF phase: `forecast` (`cfp=3`)

Итог:

- `doc:core/doc-lifecycle#A17F9C2B@v.1.3.7.3`

---

## 2. Сделка (lead/deal)

Сущность:

- `EntityId = deal:sales/enterprise-042#7B3D91E2`

Состояние:

- инкарнация: `2` (после transform стратегии)
- LC: `F2` (`lc=2`)
- CF: `4`
- CF phase: `decide` (`cfp=4`)

Итог:

- `deal:sales/enterprise-042#7B3D91E2@v.2.2.4.4`

---

## 3. Программный модуль

Сущность:

- `EntityId = sys:platform/parser-runtime#5D0E21AA`

Состояние:

- инкарнация: `3` (после архитектурного transform)
- LC: `F3` (`lc=3`)
- CF: `12`
- CF phase: `implement` (`cfp=5`)

Итог:

- `sys:platform/parser-runtime#5D0E21AA@v.3.3.12.5`

---

## 4. Переходы (иллюстрация)

Пример для документа:

1. `...@v.1.3.7.5` (`implement`)
2. `...@v.1.3.7.6` (`evaluate`)
3. `...@v.1.3.8.1` (старт нового осмысленного CF: `collect`)

При `transform`:

1. `...@v.1.6.15.6` (завершение инкарнации)
2. `...@v.2.1.1.1` (новая инкарнация, новый LC и новый CF)

---

## 5. Анти-примеры (невалидно)

1. Коммит без `task_ref/intent_ref` изменил `cf`:
- невалидно, потому что отсутствует осмысленный CF-контекст.

2. Ручной апдейт `v.1.3.7.3 -> v.1.3.8.4` без событий:
- невалидно, потому что нет подтвержденных переходов.

3. Смена `EntityId` при той же сущности:
- невалидно, потому что нарушена идентичность.

