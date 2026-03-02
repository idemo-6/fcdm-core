---
title: "Profile: Subjectivity in Machine Learning"
date: 2026-03-02
tags: [CDM, Subjectivity, profile, ML, creativity]
citekey: cdm_subjectivity_domain_ml_profile_ru_2026
---

# Profile: Subjectivity in Machine Learning

Status: `illustrative`

## 1. Контекст

- Область: CV/ML classification.
- Цель: достигнуть высокого `R` при ресурсных ограничениях.
- Критерий `R`: quality metric (например, Top-1 accuracy) при заданном latency/size.

## 2. Reference

Эталон `Ref` задается по
[[fcdm-core/theory/cdm/Specifications/System/Subjectivity-Reference-Agent-Profile|Subjectivity-Reference-Agent-Profile]].

## 3. Rule

- `R >= R(Ref)` и высокий `S(A,Ref)` -> креативное и эффективное решение.
- Высокий `S` при падении `R` -> исследовательский, но не production-режим.

## 4. Practical use

- Production selection: фильтр по `R` и рискам.
- Research selection: приоритет по `S` при минимально допустимом `R`.
