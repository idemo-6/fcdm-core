---
title: "Спецификация: Creative ChangeFlow (каноническая)"
date: 2026-03-02
tags: [CDM, CreativeChangeFlow, canonical, Subjectivity, Doubt]
citekey: cdm_creative_changeflow_canonical_ru_2026
---

# Спецификация: Creative ChangeFlow (каноническая)

## 1. Область определения

`Creative ChangeFlow` — специализированный режим `ChangeFlow`,
в котором расширение и удержание множества альтернатив в ранних фазах
используется как контролируемый источник новизны.

Режим не отменяет канонический `CF1..CF6` и не нарушает фазовые гейты.

---

## 2. Нормативные ссылки

- [[fcdm-core/theory/cdm/Specifications/ChangeFlow-6_v3|ChangeFlow-6]]
- [[fcdm-core/theory/cdm/Specifications/System/Subjectivity-Canonical|Subjectivity-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/System/Doubt-Canonical|Doubt-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/System/Viewpoint-Canonical|Viewpoint-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/System/MetaChangeFlow-Canonical|MetaChangeFlow-Canonical]]

---

## 3. Каноническое определение

Для системы `Y` в контексте `C`:

`CreativeChangeFlow(Y,C)` — режим выполнения `ChangeFlow`, где:

1. фазы раннего поиска (`collect/analyze/forecast`) расширяют пространство альтернатив;
2. коллапс выбора в `decide` может быть осознанно отложен в пределах policy;
3. `implement` выполняет ограниченное подмножество выбранных сценариев;
4. `evaluate` фиксирует не только результат, но и потери альтернатив/цену коллапса.

---

## 4. Инварианты

1. Канонические фазы `CF1..CF6` сохраняются.
2. Удержание альтернатив не может бесконечно откладывать `decide` без policy-гейта.
3. Высокая `Subjectivity` не тождественна креативности.
4. `Doubt` используется как регулятор режима, но не как единственный критерий принятия решения.
5. Переход в `implement` допустим только после валидного `decide`.

---

## 5. Граница канона

Канон не фиксирует:

- численные пороги `Doubt`;
- доменные формулы `CSI`;
- конкретные эвристики генерации альтернатив.

Эти элементы задаются в model-core и доменных профилях.

---

## 6. Связь с Subjectivity, Doubt и MetaChangeFlow

1. `Subjectivity` повышает разнообразие траекторий, но сама по себе не гарантирует креативный результат.
2. `Doubt` помогает удерживать альтернативы до обоснованного момента коллапса.
3. При неустойчивом режиме или параличе выбора может запускаться `MetaChangeFlow` по policy.

---

## 7. Модель и профили

- [[fcdm-core/theory/cdm/Specifications/System/CreativeChangeFlow-Model-Core|CreativeChangeFlow-Model-Core]]
- [[fcdm-core/theory/cdm/Specifications/System/CreativeChangeFlow-Examples|CreativeChangeFlow-Examples]]
- [[fcdm-core/theory/cdm/Specifications/System/CreativeChangeFlow-Domain-Profiles/CreativeChangeFlow-Domain-RnD-Profile|CreativeChangeFlow-Domain-RnD-Profile]]
- [[fcdm-core/theory/cdm/Specifications/System/CreativeChangeFlow-Domain-Profiles/CreativeChangeFlow-Domain-AI-Architecture-Profile|CreativeChangeFlow-Domain-AI-Architecture-Profile]]
- [[fcdm-core/theory/cdm/Specifications/System/CreativeChangeFlow-Domain-Profiles/CreativeChangeFlow-Domain-Document-Innovation-Profile|CreativeChangeFlow-Domain-Document-Innovation-Profile]]
