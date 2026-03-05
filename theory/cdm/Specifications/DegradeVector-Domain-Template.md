---
title: "Шаблон: Domain DegradeVector Specification"
date: 2026-03-05
tags: [CDM, DegradeVector, domain, template]
---

# Шаблон: Domain DegradeVector Specification

## 1. Domain

- Domain ID:
- Domain Name:
- Связанный DomainLexicon:
- Версия профиля:

---

## 2. Доноры метрик (`rr_i`)

Для каждого донора указать:
- `id`:
- физический/операционный смысл:
- исходная формула:
- диапазон до нормализации:
- нормализация в `[0,1]`:
- источник данных (dataset URL):
- код расчета (repo/file URL):

---

## 3. Агрегация в DS

- функция `Agg`:
- параметры `Agg`:
- правила весов `omega_i`:
- проверка `sum(omega_i)=1`:
- направление `DS`:
  - `0 = best`
  - `1 = worst`

---

## 4. Политика порогов

- `DS_stable`:
- `DS_warning` (опционально):
- `tau_stable_min`:
- `tau_phase_min`:
- обоснование порогов:

Примечание:
Численные пороги валидны только при наличии открытого датасета и воспроизводимого кода.

---

## 5. Runtime vs analytics

- Как определяется `runtime.result in {+1,0,-1}`:
- Правило `result=0 <=> ApplicabilityFailure`:
- Как считается `analysis.op_signal in {-1,0,+1}`:
- Mapping `op_signal -> expected Delta_DS sign`:

---

## 6. Update в CF6

Определить:
- где фиксируется `DegradeVector` snapshot;
- как вычисляется `DS`;
- как связывается с `UpdateExp`;
- какие проверки выполняются перед коммитом `CF6`.

---

## 7. Минимальные тесты домена

- T1: `DS in [0,1]` для всех валидных входов.
- T2: при `cf_phase != CF6` обновление `DegradeVector/DS` отклоняется.
- T3: `result=0` фиксируется только как `ApplicabilityFailure`.
- T4: `op_signal` не подменяет `result`.
- T5: воспроизводимость расчета (`dataset + code`).
