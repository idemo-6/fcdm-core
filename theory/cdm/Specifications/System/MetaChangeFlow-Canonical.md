---
title: "Спецификация: MetaChangeFlow (каноническая)"
date: 2026-03-02
tags: [CDM, MetaChangeFlow, canonical, Viewpoint]
citekey: cdm_metachangeflow_canonical_ru_2026
---

# Спецификация: MetaChangeFlow (каноническая)

## 1. Область определения

`MetaChangeFlow` — ChangeFlow мета-уровня, направленный на адаптацию
`Viewpoint` и операторного контура при признаках неадекватности текущей
траектории выбора.

---

## 2. Нормативные ссылки

- [[fcdm-core/theory/cdm/Specifications/System/Viewpoint-Canonical|Viewpoint-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/System/Doubt-Canonical|Doubt-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/Experience/Experience-Canonical|Experience-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/ChangeFlow-6_v3|ChangeFlow-6]]

---

## 3. Каноническое назначение

`MetaChangeFlow` применяется, когда стандартный уровень `forecast/decide`
недостаточен для устойчивого выбора и требуется пересборка
рамки принятия решений.

---

## 4. Инварианты

1. MetaChangeFlow не отменяет базовый ChangeFlow, а управляет его рамкой.
2. Изменения Viewpoint/операторов должны быть трассируемыми в графе опыта.
3. Результаты MetaChangeFlow подлежат обычной evaluate-фиксации.
4. Запуск MetaChangeFlow определяется policy-гейтами, а не произвольно.

---

## 5. Граница канона

Канон не фиксирует:

- конкретные пороги активации;
- доменные списки MetaOperators;
- глубину рекурсии.

Эти параметры задаются в policy и доменных профилях.

---

## 6. Политика запуска

Нормативная policy:

- [[fcdm-core/theory/cdm/Specifications/System/MetaChangeFlow-Trigger-Policy|MetaChangeFlow-Trigger-Policy]]
