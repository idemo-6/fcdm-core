---
title: "Спецификация: Viewpoint (каноническая)"
date: 2026-03-02
tags: [CDM, Viewpoint, canonical, ChangeOperators, Experience]
citekey: cdm_viewpoint_canonical_ru_2026
---

# Спецификация: Viewpoint (каноническая)

## 1. Область определения

Документ задает каноническое определение `Viewpoint` как мета-механизма,
ограничивающего и структурирующего доступ системы к применимым траекториям
`ChangeFlow` через доступный операторный контур.

`Viewpoint` не тождественен `Context`, но работает совместно с ним.

---

## 2. Нормативные ссылки

- [[fcdm-core/theory/cdm/Specifications/System/System-Canonical|System-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/Context/Context-Canonical|Context-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/Operators/ChangeOperators-Canonical|ChangeOperators-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/Experience/Experience-Canonical|Experience-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/ChangeFlow-6_v3|ChangeFlow-6]]

---

## 3. Каноническое определение

`Viewpoint(Y,t)` — конфигурация селекции и композиции операторов,
через которую система `Y` формирует и оценивает альтернативы изменения
в текущем контексте `C_active`.

---

## 4. Инварианты

1. `Viewpoint` влияет на `forecast/decide`, но не отменяет `Context`-применимость.
2. `Viewpoint` изменяем во времени и накапливает опытные следы.
3. Выбор в `implement` должен опираться на фазовые гейты, а не только на Viewpoint.
4. `Viewpoint` может быть объектом MetaChangeFlow-адаптации.

---

## 5. Граница канона

Канон фиксирует только смысловую роль `Viewpoint`.

Не входят в канон:

- доменные наборы операторов;
- численные параметры стохастики;
- конкретные эвристики кэширования/ранжирования.

---

## 6. Эволюция и MetaChangeFlow

- Модель эволюции: [[fcdm-core/theory/cdm/Specifications/System/Viewpoint-Evolution-Model-Core|Viewpoint-Evolution-Model-Core]]
- Канон MetaChangeFlow: [[fcdm-core/theory/cdm/Specifications/System/MetaChangeFlow-Canonical|MetaChangeFlow-Canonical]]
- Trigger Policy: [[fcdm-core/theory/cdm/Specifications/System/MetaChangeFlow-Trigger-Policy|MetaChangeFlow-Trigger-Policy]]

- Creative режим: [[fcdm-core/theory/cdm/Specifications/System/CreativeChangeFlow-Canonical|CreativeChangeFlow-Canonical]]
