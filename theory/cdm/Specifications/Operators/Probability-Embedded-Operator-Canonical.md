---
title: "Спецификация: Probability as Embedded Operator (каноническая)"
date: 2026-03-02
tags: [CDM, Operators, Probability, canonical, decide]
citekey: cdm_probability_embedded_operator_canonical_ru_2026
---

# Спецификация: Probability as Embedded Operator (каноническая)

## 1. Область определения

`Probability` задается как встроенный оператор выбора на фазе `decide`
при неполной информации, конкурирующих альтернативах или ограниченных ресурсах.

## 2. Нормативные ссылки

- [[fcdm-core/theory/cdm/Specifications/Operators/ChangeOperators-Canonical|ChangeOperators-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/ChangeFlow-6_v3|ChangeFlow-6]]
- [[fcdm-core/theory/cdm/Specifications/System/Doubt-Canonical|Doubt-Canonical]]

## 3. Каноническая формулировка

`Probability(S,R)` действует в `CF4/decide` как оператор стохастического выбора
сценария из множества `X={X_1..X_n}`:

`X_i ~ P(X_i | S,R)`, где `sum_i P(X_i | S,R)=1`.

## 4. Инварианты

1. Probability не подменяет применимость (`Applicable`).
2. Probability не выполняет физическую фиксацию изменения (`implement`).
3. Probability является оператором выбора, а не источником креативности.

## 5. Граница канона

Конкретные распределения и доменные эвристики задаются в профильном документе.
