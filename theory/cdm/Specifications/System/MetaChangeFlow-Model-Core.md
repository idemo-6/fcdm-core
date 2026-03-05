---
title: "Модель: MetaChangeFlow (core)"
date: 2026-03-04
tags: [CDM, MetaChangeFlow, model, Viewpoint, Intent, Doubt, Experience]
citekey: cdm_metachangeflow_model_core_ru_2026
---

# Модель: MetaChangeFlow (core)

## 1. Назначение

Документ задает модельный (non-canonical) слой для `MetaChangeFlow`:
рефлексивные циклы над `Viewpoint / Intent / Doubt` с фиксацией изменений в `Experience`.

Канонические инварианты и границы задаются в:
- [[fcdm-core/theory/cdm/Specifications/System/MetaChangeFlow-Canonical|MetaChangeFlow-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/System/MetaChangeFlow-Trigger-Policy|MetaChangeFlow-Trigger-Policy]]
- [[fcdm-core/theory/cdm/Specifications/ChangeFlow-6_v3|ChangeFlow-6]]
- [[fcdm-core/theory/cdm/DomainLexicon|DomainLexicon]]

Нотация:
- каноническая: `CF1..CF6`;
- доменная/профильная: `collect/analyze/forecast/decide/implement/evaluate` как алиасы к `CF1..CF6`.

---

## 2. Фазовая схема MetaChangeFlow

Каноническая форма:

`MetaCF = [CF1 => CF2 => CF3 => CF4 => CF5 => CF6]`

Доменная интерпретация (алиасы, non-canonical):

`CF1=collect, CF2=analyze, CF3=forecast, CF4=decide, CF5=implement, CF6=evaluate`

1. `CF1/collect`: фиксация trigger-condition (`Doubt > theta_meta`, низкая устойчивость выбора, повтор без прогресса).
2. `CF2/analyze`: построение `MetaViewpoint` и формулировка гипотез перестройки.
3. `CF3/forecast`: генерация и симуляция альтернатив через MetaOperators.
4. `CF4/decide`: ранжирование альтернатив по `EV`, `Doubt_post`, `M`.
5. `CF5/implement`: фиксация новой рамки (`Viewpoint/Intent-policy`) и архивирование superseded-конфигурации.
6. `CF6/evaluate`: запись результата в граф опыта и проверка post-conditions.

---

## 3. MetaOperators (модельный набор)

Базовый набор операторов мета-перестройки:
- `Split`
- `Merge`
- `Rotate`
- `Invent`
- `Prune`
- `Adjust`

Допустимый набор определяется доменным профилем и policy.

---

## 4. Рекурсия и ограничение глубины

`MetaChangeFlow` допускает рекурсивный запуск при повторной неадекватности рамки выбора.

Рекомендуемое ограничение в профилях:
- `max_depth <= 3`.

Точное значение `max_depth` остается policy-параметром.

---

## 5. Интеграция с Experience

Мета-изменение должно быть трассируемо в `Experience`:
- reuse успешных конфигураций `Viewpoint/Operators`;
- контрфактическая симуляция альтернатив в `forecast`;
- связь `superseded_by` между предыдущей и новой рамкой;
- фиксация причин запуска (`trigger_reason[]`) и критерия завершения.

---

## 6. Универсальность по классам систем (профильная интерпретация)

Классификация неканоническая и используется как прикладной профиль:

1. Класс `0-1`: нет полноценного MetaCF (обычно только `implement`-реакции).
2. Класс `2-3`: зародышевые мета-процессы (ограниченная рефлексия).
3. Класс `4`: базовая рефлексия над опытом и операторным выбором.
4. Класс `5`: полный MetaCF над `Viewpoint/Intent`.
5. Класс `6`: вложенные мета-контуры и самоэволюция правил перестройки.

---

## 7. Связь с теорией сложности (non-normative)

1. Рост вариативности `V` увеличивает комбинаторную сложность `forecast/decide`.
2. Рекурсивный MetaCF повышает риск экспоненциального ветвления поиска.
3. Ограниченные ресурсы наблюдателя требуют coarse-graining и аппроксимаций.
4. В прикладных профилях низкая `V` ведет к более простым (ближе к `P`) режимам, высокая `V` — к трудным (`NP-hard`-подобным) режимам выбора.

---

## 8. Связь с теорией информации (non-normative)

1. Генерация альтернатив в `forecast` увеличивает энтропию выбора `H`.
2. Фаза `decide` снижает `H` через отбор траектории.
3. Рекурсия временно увеличивает мета-информацию, затем снижает неопределенность после `implement`.
4. Reuse опыта уменьшает прирост `H` за счет повторного использования проверенных конфигураций.
5. `Invent`-операторы дают максимальный прирост неопределенности и требуют усиленного evidence-контроля.

---

## 9. Следствия модели

- Универсальный механизм самоулучшения рамки выбора в ODS/CDM-профилях.
- Снижение риска застревания в неэффективном `Viewpoint`.
- Ускорение архитектурной эволюции при соблюдении policy-гейтов и evidence-требований.
