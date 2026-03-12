---
title: "Policy: MetaChangeFlow Trigger"
date: 2026-03-02
tags: [CDM, MetaChangeFlow, policy, trigger]
citekey: cdm_metachangeflow_trigger_policy_ru_2026
---

# Policy: MetaChangeFlow Trigger

## 1. Назначение

Документ задает минимальные правила активации `MetaChangeFlow`.

---

## 2. Возможные сигналы (профильно настраиваются)

1. `Doubt` выше доменного порога `theta_meta`.
2. Повторяемые циклы без прогресса (например, повтор CF-паттерна > N).
3. Систематические `-1` в релевантных контекстах.
4. Рост несовместимости альтернатив при недостаточной операторной емкости.

---

## 3. Минимальный trigger-контракт

Перед запуском должны быть зафиксированы:

- `entity_id`;
- текущий `Viewpoint` snapshot;
- причины активации (`trigger_reason[]`);
- ожидаемый критерий завершения MetaChangeFlow.

---

## 4. Ограничения

1. Trigger без evidence невалиден.
2. Пороговые значения определяются доменным профилем, не каноном.
3. Рекурсия MetaChangeFlow ограничивается policy (например, `max_depth`).
