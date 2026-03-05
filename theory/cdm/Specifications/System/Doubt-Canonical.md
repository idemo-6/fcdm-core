---
title: "Спецификация: Doubt (каноническая)"
date: 2026-03-02
tags: [CDM, Doubt, canonical, Viewpoint, ChangeFlow]
citekey: cdm_doubt_canonical_ru_2026
---

# Спецификация: Doubt (каноническая)

## 1. Область определения

Документ задает каноническое определение `Doubt` как системного свойства,
характеризующего множественность релевантных альтернатив в текущем `Viewpoint`
относительно доступной операторной емкости системы.

`Doubt` не является эмоциональной категорией и не трактуется антропоморфно.

---

## 2. Нормативные ссылки

- [[fcdm-core/theory/cdm/Specifications/System/System-Canonical|System-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/ChangeFlow-6_v3|ChangeFlow-6]]
- [[fcdm-core/theory/cdm/Specifications/Operators/ChangeOperators-Canonical|ChangeOperators-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/Context/Context-Canonical|Context-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/System/Viewpoint-Canonical|Viewpoint-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/System/MetaChangeFlow-Canonical|MetaChangeFlow-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/System/CreativeChangeFlow-Canonical|CreativeChangeFlow-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/Experience/Experience-Canonical|Experience-Canonical]]

---

## 3. Каноническое определение

Для системы `Y` в контексте `C`:

`Doubt(Y,C)` — мера напряжения выбора, возникающего из сочетания:

1. количества/значимости доступных альтернатив;
2. операторной емкости системы для их обработки;
3. цены ошибки в данном контексте;
4. локально подтвержденного опыта применения операторов.

---

## 4. Инварианты

1. `Doubt >= 0`.
2. `Doubt` контекстно-зависимо: изменение `C` может изменить значение.
3. `Doubt` может использоваться как сигнал запуска дополнительного `forecast/decide` или `MetaChangeFlow`.
4. `Doubt` не заменяет phase-gates и правила применимости.

---

## 5. Граница канона

Канон фиксирует только смысл и инварианты.

Не входят в канон:

- численные пороги (`theta` и др.);
- конкретная функция вычисления;
- доменные режимы эскалации.

Эти элементы определяются в профильных документах.
Выбор расчетного профиля (`v1` simplified baseline или `v2` advanced/non-monotonic) задается в [[fcdm-core/theory/cdm/Specifications/System/Doubt-Model-Core|Doubt-Model-Core]] и доменных профилях.

---

## 6. Роль в MMCF

`Doubt` учитывается в `forecast/decide` для:

- предотвращения ложной уверенности;
- выявления ситуаций с высокой альтернативностью;
- эскалации в `MetaChangeFlow` при достижении доменного порога.

---

## 7. Модель и примеры

- Формальная модель: [[fcdm-core/theory/cdm/Specifications/System/Doubt-Model-Core|Doubt-Model-Core]]
- Примеры: [[fcdm-core/theory/cdm/Specifications/System/Doubt-Examples|Doubt-Examples]]
- Доменные профили: [[fcdm-core/theory/cdm/Specifications/System/Doubt-Domain-Profiles/Doubt-Domain-AI-Decision-Profile|Doubt-Domain-AI-Decision-Profile]], [[fcdm-core/theory/cdm/Specifications/System/Doubt-Domain-Profiles/Doubt-Domain-Organization-Decision-Profile|Doubt-Domain-Organization-Decision-Profile]], [[fcdm-core/theory/cdm/Specifications/System/Doubt-Domain-Profiles/Doubt-Domain-Document-Revision-Profile|Doubt-Domain-Document-Revision-Profile]]
