---
title: "Спецификация: DegradeVector (каноническая)"
date: 2026-03-04
tags: [CDM, DegradeVector, DegradeScore, canonical, LifeCycle]
citekey: cdm_degradevector_canonical_ru_2026
---

# Спецификация: DegradeVector (каноническая)

## 1. Область определения

Документ задает каноническое определение `DegradeVector` и `DegradeScore (DS)`
как операционных метрик состояния системы в контуре `LifeCycle-6`.

`DegradeVector` хранит многомерную доменную информацию, `DS` является ее
канонической скалярной проекцией для фазовой логики.

---

## 2. Нормативные ссылки

- [[fcdm-core/theory/cdm/Specifications/LifeCycle-6_v2|LifeCycle-6]]
- [[fcdm-core/theory/cdm/Specifications/ChangeFlow-6_v3|ChangeFlow-6]]
- [[fcdm-core/theory/cdm/Specifications/CF-LC-Evaluate|CF-LC-Evaluate]]
- [[fcdm-core/theory/cdm/DomainLexicon|DomainLexicon]]

---

## 3. Канонические определения

1. `DegradeVector = <rr_1, ..., rr_n>`, где `rr_i` — нормированные доменные
   компоненты деградации.
2. `DS = Agg(DegradeVector, policy)` — скалярная агрегированная метрика.
3. Каноническая шкала `DS`:
   - `DS = 0` — лучший (наименее деградированный) режим;
   - `DS = 1` — худший (предельная деградация) режим.

---

## 4. Инварианты

1. `DS in [0,1]`.
2. `DegradeVector` и `DS` обновляются только в `CF6` (`evaluate`).
3. Агрегация `Agg` должна быть явной и воспроизводимой в доменном профиле.
4. Канон не фиксирует конкретную формулу `Agg` и численные пороги фаз.

---

## 5. Связь с runtime-тринарностью

`Result in {+1,0,-1}` остается runtime-семантикой ChangeFlow:
- `+1` — применимо и успешно;
- `0` — `ApplicabilityFailure`;
- `-1` — применимо, но деградационно/неуспешно.

Нейтральный или смешанный вклад метрик должен кодироваться отдельным
аналитическим сигналом (например, `op_signal`), но не через `Result=0`.

---

## 6. Граница канона

Канон не фиксирует:
- набор доменных доноров метрик;
- веса агрегации;
- конкретные пороги `DS_stable`, `DS_warning`, `tau_*`.

Эти элементы принадлежат модельным и доменным профильным документам.

Связанные документы:
- [[fcdm-core/theory/cdm/Specifications/Aggregate-Metrics-Model-Core|Aggregate-Metrics-Model-Core]]
- [[fcdm-core/theory/cdm/Specifications/DegradeVector-Machine-Contract|DegradeVector-Machine-Contract]]
- [[fcdm-core/theory/cdm/Specifications/DegradeVector-Domain-Template|DegradeVector-Domain-Template]]
- [[fcdm-core/theory/cdm/Specifications/DegradeVector-Conformance-Minimal|DegradeVector-Conformance-Minimal]]
