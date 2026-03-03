---
title: "Migration Note: Versioning Governance Split (MMCF -> CDM -> FROR)"
date: 2026-03-03
tags: [CDM, MMCF, versioning, migration-note, governance]
citekey: cdm_versioning_migration_note_2026_03
---

# Migration Note: Versioning Governance Split (2026-03)

## 1. Что изменено

В марте 2026 введена двухуровневая модель управления versioning:

1. `MMCF` хранит **методологический канон** versioning.
2. `CDM` хранит **профиль применения** канона к LC/CF-структуре CDM.
3. `FROR` использует профиль CDM как операционную интеграцию в своем слое.

Физическое расположение файлов CDM сохранено (мягкая миграция без переноса
путей и без ломки ссылок Obsidian).

---

## 2. Целевая иерархия

`MMCF canonical -> CDM profile -> FROR usage`

### 2.1 MMCF canonical

- [MMCF Versioning Canonical](../../../../../mmcf-docs/methodology/Versioning-Canonical.md)
- [MMCF Claim Maturity Canonical](../../../../../mmcf-docs/methodology/Claim-Maturity-Canonical.md)

### 2.2 CDM profile

- [[fcdm-core/theory/cdm/Specifications/Versioning/Versioning-Canonical|Versioning-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/Versioning/Version-Derivation-Policy|Version-Derivation-Policy]]
- [[fcdm-core/theory/cdm/Specifications/Claim-Maturity-Profile|Claim-Maturity-Profile]]

### 2.3 FROR usage

- [[fcdm-core/theory/fror/FROR_architecture_v2|FROR Architecture V2]]

---

## 3. Принцип разделения ответственности

1. MMCF отвечает за норму governance:
   state-derived, audit/override, независимость осей `EntityVersion` и
   `ClaimStatus`.
2. CDM отвечает за профильные детали:
   формат `v.<inc>.<lc>.<cf>.<cfp>`, event log derivation и LC/CF-гейты.
3. FROR отвечает за применение этого механизма к исследовательским
   утверждениям и архитектуре слоев.

---

## 4. Что остается неизменным

1. Существующие пути CDM-файлов `Versioning/*`.
2. Формула версии CDM `EntityId@v.<inc>.<lc>.<cf>.<cfp>`.
3. Совместимость с текущими Obsidian wikilinks.

---

## 5. Практический эффект

1. Versioning формально принадлежит governance-слою MMCF.
2. CDM остается источником профильных operational-правил.
3. FROR/CDM получают единый язык для версий сущности и зрелости тезисов
   без смешения этих осей.
