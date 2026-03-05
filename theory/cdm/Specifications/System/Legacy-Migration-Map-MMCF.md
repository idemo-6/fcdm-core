---
title: "Legacy -> CDM/MMCF Migration Map (phase bundle)"
date: 2026-03-02
tags: [CDM, MMCF, migration, legacy, mapping]
citekey: cdm_mmcf_legacy_migration_map_ru_2026
---

# Legacy -> CDM/MMCF Migration Map

## 1. Scope

Документ фиксирует разнесение legacy-материалов по целевой структуре CDM/MMCF.

## 2. Mapping

| Legacy doc | Target placement | Status |
|---|---|---|
| 2.2.2 Эволюция Viewpoint | `System/Viewpoint-Evolution-Model-Core.md` | integrated |
| 2.2.10 MetaChangeFlow адаптации Viewpoint | `System/MetaChangeFlow-Canonical.md`, `System/MetaChangeFlow-Trigger-Policy.md` | integrated |
| 2.2.11 Мета-процессы (MetaChangeFlow) | `System/MetaChangeFlow-Model-Core.md` | integrated |
| 2.2.12 Агрегатные метрики (универсальная рамка) | `DegradeVector-Canonical.md`, `Aggregate-Metrics-Model-Core.md`, `DegradeVector-Machine-Contract.md`, `DegradeVector-Domain-Template.md`, `DegradeVector-Conformance-Minimal.md` | integrated |
| 2.2.8 Интуиция как fast-path | `System/Viewpoint-Domain-Profiles/Viewpoint-Domain-Intuition-FastPath-Profile.md` | created |
| 2.2.7 Эмоция как рефлекс | `System/Viewpoint-Domain-Profiles/Viewpoint-Domain-Emotion-Reflex-Profile.md` | created |
| Пример 05: искусство (S/творчество) | `System/Subjectivity-Domain-Profiles/Subjectivity-Domain-Art-Creativity-Profile.md` | created |
| 1.3.6 Вероятность | `Operators/Probability-Embedded-Operator-Canonical.md`, `Operators/Probability-Decision-Profile.md` | created |
| 2.4.3.1 Творческий процесс как ChangeFlow | `System/CreativeChangeFlow-Canonical.md`, `System/CreativeChangeFlow-Model-Core.md`, `System/CreativeChangeFlow-Examples.md` | integrated |

| 2.4.1.2 Subjectivity in ML | `System/Subjectivity-Domain-Profiles/Subjectivity-Domain-ML-Creativity-Profile.md` | created |
| 2.4.1.4 Subjectivity in Corporate Strategy | `System/Subjectivity-Domain-Profiles/Subjectivity-Domain-Corporate-Strategy-Profile.md` | created |
| 2.4.1.3 Subjectivity in Population Biology | `System/Subjectivity-Domain-Profiles/Subjectivity-Domain-Biology-Population-Profile.md` | created |

## 3. Rule

Нормативные определения размещаются в `Specifications/*Canonical` и `*Model-Core`.
Доменные и прикладные интерпретации — только в `*Domain-Profiles` и `*Examples`.
