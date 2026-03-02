---
title: "Спецификация: Subjectivity (каноническая)"
date: 2026-03-02
tags: [CDM, Subjectivity, canonical, ChangeFlow, Context]
citekey: cdm_subjectivity_canonical_ru_2026
---

# Спецификация: Subjectivity (каноническая)

## 1. Область определения

Документ задает каноническое определение `Subjectivity` как системного свойства в CDM.

`Subjectivity` описывает функциональное расхождение траекторий изменения между системами при заданном контексте и не трактуется как антропоморфное, феноменологическое или эмоциональное свойство.

---

## 2. Нормативные ссылки

- [[fcdm-core/theory/cdm/Specifications/System/System-Canonical|System-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/Operators/ChangeOperators-Canonical|ChangeOperators-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/Context/Context-Canonical|Context-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/ChangeFlow-6_v3|ChangeFlow-6]]

---

## 3. Каноническое определение

Для систем `A` и `B` в контексте `C`:

`Subjectivity(A,B,C)` — мера расхождения доступных и применимых траекторий `ChangeFlow`, обусловленного:

- различием инструментария (`ChangeOperators`/функции/процедуры);
- различием контекстной релевантности;
- различием качества реализации операторов.

---

## 4. Инварианты

1. `S(A,B,C) >= 0`.
2. `S(A,B,C) = 0` только при функциональной эквивалентности релевантного инструментария в `C`.
3. `S` контекстно-зависима: изменение `C` может изменить значение `S`.
4. `S` не является индикатором сознания, эмоций или внутреннего переживания.

---

## 5. Сравнение с эталоном

Канон допускает сравнение вида:

- `S(A,B,C)` (межсистемное);
- `S(A,Ref,C)` (с эталонной системой).

`Ref` задается профильным документом домена и не определяется данным каноном.

---

## 6. Граница канона

Канон фиксирует только смысл и инварианты `Subjectivity`.

Не входят в канон:

- конкретные численные пороги;
- выбор функции нормировки;
- доменные критерии эталона;
- организационные правила принятия решений на основе `S`.

Эти элементы задаются профильными документами.

---

## 7. Связь с управлением изменениями

В CDM/MMCF `Subjectivity` может влиять на выбор траектории в `forecast/decide`,
но не заменяет:

- фазовые гейты,
- требования доказательств,
- валидацию применимости.

---

## 8. Модель и примеры

- Формальная модель: [[fcdm-core/theory/cdm/Specifications/System/Subjectivity-Model-Core|Subjectivity-Model-Core]]
- Примеры: [[fcdm-core/theory/cdm/Specifications/System/Subjectivity-Examples|Subjectivity-Examples]]
- Доменные профили: [[fcdm-core/theory/cdm/Specifications/System/Subjectivity-Domain-Profiles/Subjectivity-Domain-AI-Risk-Profile|Subjectivity-Domain-AI-Risk-Profile]], [[fcdm-core/theory/cdm/Specifications/System/Subjectivity-Domain-Profiles/Subjectivity-Domain-Organization-Profile|Subjectivity-Domain-Organization-Profile]], [[fcdm-core/theory/cdm/Specifications/System/Subjectivity-Domain-Profiles/Subjectivity-Domain-Document-Profile|Subjectivity-Domain-Document-Profile]]
