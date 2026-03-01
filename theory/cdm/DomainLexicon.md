---
authors:
  - Yakov
citekey: yakov_domainlexicon_2026
date: 2026-02-26
tags:
  - CDM
  - LifeCycle-6
  - ChangeFlow-6
  - DomainLexicon
title: "DomainLexicon: Domain-Specific Interpretation of LifeCycle and ChangeFlow Phases"
---

# DomainLexicon: доменно-специфическая интерпретация фаз

## 1. Назначение

**DomainLexicon** — это отображение канонических фаз LifeCycle (`F₁…F₆`) и ChangeFlow (`CF₁…CF₆`) в терминологию конкретного предметного домена при сохранении операционных инвариантов.

Канонические символы (`F*`, `CF*`) являются единственным источником формального смысла.  
Доменная терминология носит исключительно интерпретационный характер и не влияет на верификацию.

---

## 2. Канонический принцип

Фаза определяется не словом, а принадлежностью состояния области DegradeVector и выполнением операционных условий:

- `exists`
- `DS`
- `τ`
- PhaseTransition

Следовательно:

> DomainLexicon не определяет фазу; он лишь присваивает человекочитаемое имя канонической фазе.

---

## 3. Формальное определение

Пусть:

F = {F₁,…,F₆},  
C = {CF₁,…,CF₆}

DomainLexicon определяется отображением:

φ_D : (F ∪ C) → Terms_D

где `Terms_D` — множество терминов домена D.

---

## 4. Требования валидности

DomainLexicon считается корректным тогда и только тогда, когда выполняются условия:

### (V1) Сохранение функциональной роли

Каждый термин обязан ссылаться на канонические ограничения:

- для LifeCycle: `(exists, DS, τ)`
- для ChangeFlow: инварианты фаз (selection, commit, feedback)

### (V2) Наличие оператора наблюдения

Для каждой фазы должен быть указан наблюдаемый оператор:

O_i : Ω_D → ℝ^k

позволяющий экспериментально различить фазу.

Отсутствие наблюдаемого оператора делает отображение недействительным.

### (V3) Инъективность ролей

Разные канонические фазы не могут отображаться в один термин без явного указания слияния (`merge`).

### (V4) Независимость канона

Изменение DomainLexicon не влияет на:

- фазовую топологию
- теорему фазовой полноты
- алгоритмы верификации

---

## 5. Политика слияния фаз (merge)

В некоторых доменах допускается объединение фаз:

merge: {F_i, F_j} → term

Однако:

1. Слияние не изменяет каноническое число фаз.
2. Для формальной проверки должны существовать скрытые подфазы.
3. Потеря различимости ролей считается понижением разрешения наблюдения, а не опровержением теории.

---

## 6. Структура YAML-описания

```yaml
domain: "quantum_computing"

lifecycle:
  F1:
    term: "reset"
    observable: "population initialization fidelity"
    constraints: ["exists:false->true", "DS=1"]

  F2:
    term: "coherent_load"
    observable: "coherence build-up"
    constraints: ["DS decreasing"]

  F3:
    term: "logical_run"
    observable: "logical error rate plateau"
    constraints: ["DS<=0.2", "tau>=tau_stable_min"]

  F4:
    term: "error_drift"
    observable: "error accumulation slope"
    constraints: ["DS increasing"]

  F5:
    term: "uncorrectable_failure"
    observable: "logical failure event"
    constraints: ["DS=1"]

  F6:
    term: "measurement_or_reset"
    observable: "state collapse / reinitialization"
    constraints: ["exists=false or new_tag"]

changeflow:
  CF1:
    term: "syndrome_acquire"
    invariant: "state acquisition"

  CF2:
    term: "decode"
    invariant: "entropy reduction"

  CF3:
    term: "predict_chain"
    invariant: "trajectory projection"

  CF4:
    term: "choose_correction"
    invariant: "unique branch selection"

  CF5:
    term: "apply_recovery"
    invariant: "irreversible commit"

  CF6:
    term: "fidelity_update"
    invariant: "feedback to DS"
```

---

## 7. Связь DomainLexicon с LifeCycle и ChangeFlow

Связь осуществляется через две операции:

### (1) Индексация процессов фазой

π : CF → F

Каждый ChangeFlow происходит внутри некоторой фазы LifeCycle.

### (2) Обратная связь

Фаза `CF₆` — единственная точка влияния ChangeFlow на LifeCycle:

CF₆ → DS_update

Это связывает динамику изменений с глобальной топологией существования.

---

## 8. Фальсифицируемость через DomainLexicon

Теория LifeCycle-6 считается опровергнутой для домена D, если:

при достаточной инструментальной разрешающей способности невозможно определить наблюдаемый оператор хотя бы для одной канонической фазы.

Таким образом универсальность имеет экспериментальный, а не семантический характер.

---

## 9. Онтологический принцип

Разделение канона и доменной лексики реализует принцип:

> Онтология фаз инвариантна; терминология зависит от наблюдателя.

---

## 10. Заключение

DomainLexicon обеспечивает:

- отсутствие антропоморфности канона
- переносимость между дисциплинами
- машиночитаемость
- экспериментальную проверяемость
- совместимость с LifeCycle ⊕ ChangeFlow дуализмом

