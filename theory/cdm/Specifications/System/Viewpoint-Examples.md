---
title: "Примеры: Viewpoint и MetaChangeFlow"
date: 2026-03-02
tags: [CDM, Viewpoint, MetaChangeFlow, examples]
citekey: cdm_viewpoint_metachangeflow_examples_ru_2026
---

# Примеры: Viewpoint и MetaChangeFlow

## 1. Стандартный цикл без meta

- `Doubt` ниже порога.
- Система проходит `forecast -> decide -> implement`.
- Viewpoint обновляется инкрементально через `evaluate`.

## 2. Цикл с meta-активацией

- Зафиксирован высокий `Doubt` и повтор неуспешных траекторий.
- Запускается `MetaChangeFlow`.
- Пересобирается Viewpoint/операторные композиции.
- Базовый ChangeFlow продолжается с обновленной рамкой.

## 3. Анти-пример

- Запуск MetaChangeFlow без trigger-evidence и policy-гейта.
- Невалидно в каноническом режиме.
