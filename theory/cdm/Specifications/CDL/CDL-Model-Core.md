---
title: "Модель: CDL Core (междоменная)"
date: 2026-02-28
tags: [CDM, CDL, model, Context, Experience]
citekey: cdm_cdl_model_core_ru_2026
---

# Модель: CDL Core (междоменная)

## 1. Назначение

Документ задает междоменную модель вычисления применимости и классификации `Result=0` в рамках CDL.

---

## 2. Пространства

- `SemanticSpace(C)` — множество утверждений, имеющих смысл в контексте `C`.
- `Defined(P, C)` — предикат достаточной определенности утверждения в контексте.
- `Applicable(Intent, C_active, LC_phase)` — предикат реализуемости `Intent`.

---

## 3. ApplicabilityFailure

Вводится общий класс:

`ApplicabilityFailure(Intent, C_active, LC_phase) := not Applicable(Intent, C_active, LC_phase)`.

Декомпозиция:

1. `AF_sem`: `P notin SemanticSpace(C_active)` или несогласуемость смыслов.
2. `AF_epi`: утверждение в `SemanticSpace`, но недостаточно данных.
3. `AF_sto`: стохастическая неразличимость/неустойчивость решения в доступном горизонте.

Иерархия:

`AF_sem subset ApplicabilityFailure`  
`AF_epi subset ApplicabilityFailure`  
`AF_sto subset ApplicabilityFailure`.

---

## 4. Связь с Truth

`Truth(P, C) = M_sem <=> AF_sem(P, C)`.

`Truth(P, C)` не определяет напрямую `AF_epi` и `AF_sto`; они проявляются на уровне выполнения и оценки.

---

## 5. Связь с Experience

Операционный слой:

`Experience_runtime in {+1, 0, -1}`.

Семантическая интерпретация:

`Experience_runtime = 0 <=> ApplicabilityFailure`.

Аналитический слой (`evaluate`):

`Classify0(0) -> {AF_sem, AF_epi, AF_sto, mixed}`.

---

## 6. Минимальный алгоритм evaluate

1. Проверка семантической принадлежности (`AF_sem`).
2. Проверка достаточности данных (`AF_epi`).
3. Проверка стохастической устойчивости/разрешимости (`AF_sto`).
4. Маркировка причины `0` для обучения и последующего выбора `ChangeFlow`.

---

## 7. Координационный контекст

Если `Ci` и `Cj` порождают неразрешимую дивергенцию для одного `Intent`, вводится координационный контекст `C_coord`:

- задает правило приоритета;
- задает трансляцию между `SemanticSpace(Ci)` и `SemanticSpace(Cj)`;
- уменьшает `Delta_C`.
