---
title: "Примеры: Creative ChangeFlow"
date: 2026-03-02
tags: [CDM, CreativeChangeFlow, examples]
citekey: cdm_creative_changeflow_examples_ru_2026
---

# Примеры: Creative ChangeFlow

## 1. R&D задача

- В `forecast` построено 12 альтернативных сценариев.
- `decide` отложен до прохождения внешнего экспертного review.
- В `implement` ушли 2 сценария.
- `evaluate` зафиксировал `Result=+1`, а также стоимость отказа от 10 альтернатив.

## 2. Архитектура AI-системы

- Высокий `Doubt` при конкуренции архитектур.
- Активирован `MetaChangeFlow` для пересборки Viewpoint и operator-selection policy.
- После meta-перехода принято устойчивое решение и выполнен `implement`.

## 3. Анти-примеры

1. Бесконечный brainstorming без `decide` и без trigger-policy.
2. Ранний `decide` при искусственно заниженном `Doubt`, приводящий к шаблонному решению.
3. Высокий `S` при нулевом `overlap(O_forecast, O_implement)` (идеи не реализуемы).
