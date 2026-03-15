# CDM Index

Навигационный вход в корпус `CDM`.

Цель этого файла:

1. показать `CDM` как канонический execution layer;
2. отделить канон от профилей, DSL и прикладных интерпретаций;
3. помочь читать `CDM` в правильной вертикали:
   `FROR -> CDM -> MMCF`.

## 1. Что такое `CDM`

`CDM` в текущем корпусе задает не delivery workflow и не team ritual layer, а
каноническую логику исполнения изменения.

Его центральные сущности:

1. `LifeCycle`
2. `ChangeFlow`
3. `PhaseTransition`
4. `Intent`
5. `Context`
6. `Experience`
7. `System`

Рабочая формула:

- `FROR` задает инварианты;
- `CDM` задает каноническую процессную морфологию;
- applied operational systems строятся уже поверх `CDM`.

## 2. Основной канон

### 2.1 Core canonical specs

- [LifeCycle-6](./Specifications/LifeCycle-6_v2.md)
- [ChangeFlow-6](./Specifications/ChangeFlow-6_v3.md)
- [Intent](./Specifications/Intent-1.1.5.md)
- [Context Canonical](./Specifications/Context/Context-Canonical.md)
- [CtxL Canonical](./Specifications/CtxL/CtxL-Canonical.md)
- [Experience Canonical](./Specifications/Experience/Experience-Canonical.md)
- [System Canonical](./Specifications/System/System-Canonical.md)
- [PhaseTransition Overview](./Specifications/PhaseTransition_Specifications/PhaseTransition_Overview.md)

### 2.2 Supporting canonical / minimality layer

- [CDM-v2-Transition-Spec](./Specifications/CDM-v2-Transition-Spec.md)
- [CDM-v2-Minimality-Theorem](./Specifications/CDM-v2-Minimality-Theorem.md)
- [CDM-v2-Minimality-Canonical-Short](./Specifications/CDM-v2-Minimality-Canonical-Short.md)
- [CF-LC-Evaluate](./Specifications/CF-LC-Evaluate.md)

## 3. Governance and boundaries

- [Canonical-DSL-Governance](./Specifications/Governance/Canonical-DSL-Governance.md)
- [Claim-Maturity-Profile](./Specifications/Claim-Maturity-Profile.md)
- [CDM-v2-Conformance-Minimal](./Specifications/CDM-v2-Conformance-Minimal.md)

Этот слой важен, потому что `CDM` уже различает:

1. канонический смысловой слой;
2. machine / DSL representation;
3. profile-level изменения;
4. claim maturity.

## 4. System and advanced canonical packages

- [Identity-Canonical](./Specifications/System/Identity-Canonical.md)
- [Subjectivity-Canonical](./Specifications/System/Subjectivity-Canonical.md)
- [Doubt-Canonical](./Specifications/System/Doubt-Canonical.md)
- [Viewpoint-Canonical](./Specifications/System/Viewpoint-Canonical.md)
- [MetaChangeFlow-Canonical](./Specifications/System/MetaChangeFlow-Canonical.md)
- [CreativeChangeFlow-Canonical](./Specifications/System/CreativeChangeFlow-Canonical.md)

Эти пакеты нужно читать уже после базового канона `LifeCycle / ChangeFlow /
Intent / Context / System`.

## 5. Domain portability

- [DomainLexicon](./DomainLexicon.md)
- [DomainMapping/cf](./DomainMapping/cf)
- [DomainMapping/lc](./DomainMapping/lc)
- [DomainMapping/pt](./DomainMapping/pt)

Этот слой показывает, как `CDM` переносится между доменами без
переопределения канонических инвариантов.

## 6. Bridge to FROR

Ключевой переходный документ:

- [FROR <-> CDM bridge](./bridge/FROR_CDM_bridge.md)

Именно он фиксирует, как:

1. `FROR` дает инварианты;
2. `CDM` materialize'ит их в канонической логике исполнения.

## 7. Как читать `CDM`

### 7.1 Для нового читателя

1. [CDM_CANONICAL_STATUS_AND_POSITIONING](./CDM_CANONICAL_STATUS_AND_POSITIONING.md)
2. [LifeCycle-6](./Specifications/LifeCycle-6_v2.md)
3. [ChangeFlow-6](./Specifications/ChangeFlow-6_v3.md)
4. [Intent](./Specifications/Intent-1.1.5.md)
5. [Context Canonical](./Specifications/Context/Context-Canonical.md)
6. [System Canonical](./Specifications/System/System-Canonical.md)

### 7.2 Для читателя со стороны `FROR`

1. [FROR <-> CDM bridge](./bridge/FROR_CDM_bridge.md)
2. [ChangeFlow-6](./Specifications/ChangeFlow-6_v3.md)
3. [LifeCycle-6](./Specifications/LifeCycle-6_v2.md)
4. [PhaseTransition Overview](./Specifications/PhaseTransition_Specifications/PhaseTransition_Overview.md)

### 7.3 Для прикладного слоя

После базового канона уже имеет смысл переходить в `mmcf-docs`, а не
считывать `CDM` как готовую operational methodology.

## 8. Что важно не перепутать

1. `CDM` не является просто DSL или parser-profile.
2. `CDM` не равен `MMCF`.
3. `CDM` не заменяет `FROR`, а реализует его инварианты в канонической
   процессной логике.
4. Доменные алиасы не заменяют канонические обозначения.
5. Team workflows и tool mappings живут уже выше этого слоя.
