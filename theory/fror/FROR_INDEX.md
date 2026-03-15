# FROR Index

Навигационный вход в корпус `FROR`.

Цель этого файла:

1. быстро показать структуру слоя `FROR`;
2. развести `Core`, `Criteria`, `Profiles`, `Experiments` и `Overview`;
3. не дать conjectural веткам выглядеть как уже доказанное ядро.

## 1. Что такое `FROR`

`FROR` в текущем корпусе читается как кандидат на фундаментальный
инвариантный каркас для систем, где:

1. ресурс различения конечен;
2. фиксация неинъективна на множестве альтернатив;
3. выбор и commit имеют цену;
4. точный rollback становится ресурсно дорогим;
5. наблюдаемая необратимость возникает как эффективный, а не обязательно
   абсолютный режим.

Короткая формула:

`finite distinguishability -> fixation/coarse-graining -> hidden alternatives -> rollback deficit -> effective irreversibility`

## 2. Слои корпуса

### 2.1 Core

Основной вход:

- [FROR_architecture_v2](./FROR_architecture_v2.md)
- [FROR_main](./FROR_main.md)
- [FROR_axioms_v0_2](./FROR_axioms_v0_2.md)
- [FROR_resource_layer](./FROR_resource_layer.md)

Здесь находится:

1. базовый vocabulary `Omega, Sigma, F, c_fix, tau`;
2. конечность ресурса различения;
3. неинъективная фиксация;
4. эффективная необратимость как следствие дефицита различимости.

### 2.2 Criteria

- [FROR_normalizations_invariants](./FROR_normalizations_invariants.md)
- [FROR_distinguishability_resource_threshold](./FROR_distinguishability_resource_threshold.md)
- [claims_registry](./claims_registry.yaml)
- [claim_event_log](./claim_event_log.yaml)
- [FROR_claims_git_workflow](./FROR_claims_git_workflow.md)

Здесь находятся:

1. инварианты FROR;
2. anti-hack constraints;
3. claim maturity;
4. правила фальсификации и порогов.

### 2.3 Domain portability

- [FROR_DomainLexicon](./FROR_DomainLexicon.md)
- [DomainMapping/fror](./DomainMapping/fror)

Этот слой нужен не для переименования канона, а для междоменной проверки его
переносимости.

### 2.4 Experiments and registries

- [FROR_experiment_registry](./FROR_experiment_registry.md)
- [FROR_class_measurement](./FROR_class_measurement.md)
- [FROR_ds3_attractor](./FROR_ds3_attractor.md)

Это слой исследовательской программы, а не канон.

### 2.5 Profiles

Examples:

- [FROR_hilbert_profile](./FROR_hilbert_profile.md)
- [FROR_Born_rule](./FROR_Born_rule.md)
- [FROR_measurement_profile](./FROR_measurement_profile.md)
- [FROR_schrodinger_profile](./FROR_schrodinger_profile.md)
- [FROR_dual_layer_profile](./FROR_dual_layer_profile.md)
- [FROR_agency_profile](./FROR_agency_profile.md)
- [FROR_thermo_profile](./FROR_thermo_profile.md)

Здесь находятся domain- or interpretation-level extensions с разной зрелостью.

### 2.6 Conjectural structural branches

- [FROR_3plus1_phase](./FROR_3plus1_phase.md)
- [FROR_SLOT](./FROR_SLOT.md)

Эти ветки важны, но не должны читаться как уже доказанное ядро.

### 2.7 Overviews and protocol contours

- [FROR_unification_overview](./FROR_unification_overview.md)
- [FROR_quantum_protocol_contour](./FROR_quantum_protocol_contour.md)

Это навигационные и protocol-level файлы. Они не повышают зрелость claims сами
по себе.

## 3. Какой маршрут чтения оптимален

### 3.1 Для нового читателя

1. [FROR_THEORY_STATUS_AND_VALIDATION_STANCE](./FROR_THEORY_STATUS_AND_VALIDATION_STANCE.md)
2. [FROR_architecture_v2](./FROR_architecture_v2.md)
3. [FROR_main](./FROR_main.md)
4. [FROR_normalizations_invariants](./FROR_normalizations_invariants.md)
5. [FROR_experiment_registry](./FROR_experiment_registry.md)

### 3.2 Для доменного специалиста

1. [FROR_THEORY_STATUS_AND_VALIDATION_STANCE](./FROR_THEORY_STATUS_AND_VALIDATION_STANCE.md)
2. [FROR_DomainLexicon](./FROR_DomainLexicon.md)
3. relevant file in [DomainMapping/fror](./DomainMapping/fror)
4. [FROR_experiment_registry](./FROR_experiment_registry.md)

### 3.3 Для перехода к каноническому execution layer

1. [FROR <-> CDM bridge](../cdm/bridge/FROR_CDM_bridge.md)
2. then `CDM` canonical specs

## 4. Что здесь важно не перепутать

1. `FROR` не нужно читать как уже завершенную универсальную физическую теорию.
2. Quantum-like stack не является доказательством квантовой механики.
3. Междоменная переносимость — это отдельный проверяемый claim, а не
   автоматическое следствие красивой терминологии.
4. Чем дальше файл от `Core`, тем сильнее он должен читаться через его
   maturity status.

## 5. Связь с более широким стеком

Рабочая вертикаль корпуса:

1. `FROR` — инвариантный фундаментальный слой;
2. `CDM` — каноническая логика исполнения изменения;
3. `MMCF` — applied/operational/governance layer поверх `CDM`.

Поэтому `FROR` — не operational methodology, а основание, на котором
дальнейшие прикладные слои только строятся.
