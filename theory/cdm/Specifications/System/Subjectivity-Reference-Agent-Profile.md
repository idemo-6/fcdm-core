---
title: "Profile: Subjectivity Reference Agent (Ref)"
date: 2026-03-02
tags: [CDM, Subjectivity, profile, reference-agent, Ref]
citekey: cdm_subjectivity_reference_agent_profile_ru_2026
---

# Profile: Subjectivity Reference Agent (Ref)

## 1. Назначение

Профиль задает требования к эталонному агенту `Ref` для вычисления
абсолютной субъективности:

`S_A = S(A,Ref,C)`

в фиксированном контексте `C`.

---

## 2. Требования к Ref

Для заданного контекста `C` эталонный агент `Ref` должен удовлетворять:

1. Максимально полному и релевантному набору операторов для `C`.
2. Для релевантного инструмента `i`:
   - `R_i(C,Ref)=1.0`;
   - `Q_i(C,Ref)=1.0` или `max-known` (в пределах текущего уровня знаний).
3. Выбор траектории `ChangeFlow` оптимизирует доменный критерий результативности `R`.

---

## 3. Режимы использования

1. Абсолютная оценка: `S(A,Ref,C)`.
2. Сравнение систем через общий `Ref` в том же `C`.
3. Оценка креативности только в паре с результатом (`R + S`).

---

## 4. Ограничения

1. `Ref` может быть виртуальной вычислительной конструкцией.
2. При изменении границ контекста `C` или базы знаний `Ref` пересчитывается.
3. Использование устаревшего `Ref` должно помечаться как исторический режим сравнения.

---

## 5. Инварианты качества

1. `Ref` должен быть воспроизводимым (явная спецификация профиля).
2. Критерии построения `Ref` должны быть прозрачны для аудита.
3. Нельзя смешивать разные `Ref` в одной сравнительной метрике без нормализации.

---

## 6. Связанные документы

- [[fcdm-core/theory/cdm/Specifications/System/Subjectivity-Canonical|Subjectivity-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/System/Subjectivity-Model-Core|Subjectivity-Model-Core]]
- [[fcdm-core/theory/cdm/Specifications/System/Subjectivity-Domain-Profiles/Subjectivity-Domain-Art-Creativity-Profile|Subjectivity-Domain-Art-Creativity-Profile]]
