# FROR: Архитектура V2 (Core / Criteria / Profiles / Experiments)

## Назначение

Документ фиксирует целевую структуру FROR по варианту V2:
- `Core` --- канонические определения, аксиомы и теоремы;
- `Criteria` --- условия корректности, фальсификации и границы применимости;
- `Profiles` --- доменные нормализации без изменения канона;
- `Experiments` --- измерители и протоколы проверки гипотез.

Эта схема снижает "размытость": источник истины для каждого утверждения
фиксируется в одном слое.

------------------------------------------------------------------------

## 1) Core (канон)

Файлы:
- [FROR_axioms_v0_2](./FROR_axioms_v0_2.md)
- [FROR_main](./FROR_main.md)

Что хранится:
- базовые объекты (`Ω, Σ, F, c, τ`);
- аксиомы (`A1..A5`);
- выводимые теоремы уровня канона (например, порог трёхклассовой репрезентации).

Правило:
- здесь формулируются только канонические утверждения;
- экспериментальные параметры и доменные интерпретации сюда не вносятся.

------------------------------------------------------------------------

## 2) Criteria (валидность и границы)

Файлы:
- [FROR_normalizations_invariants](./FROR_normalizations_invariants.md)
- [FROR_symmetry_memory_threshold](./FROR_symmetry_memory_threshold.md)
- [Claim-Maturity-Profile](../cdm/Specifications/Claim-Maturity-Profile.md)
- [claims_registry](./claims_registry.yaml)

Что хранится:
- инварианты FROR;
- требования к корректной нормализации (`C1..C5`);
- критерии фальсификации и пороговые условия (например, память/симметрия);
- правила зрелости утверждений (`Conjecture/Protocol/Validated/Core`).

Правило:
- если утверждение не проходит по критериям этого слоя, оно не считается
  валидной FROR-нормализацией.

------------------------------------------------------------------------

## 3) Profiles (доменные отображения)

Файлы:
- [FROR_DomainLexicon](./FROR_DomainLexicon.md)
- [FROR_thermo_profile](./FROR_thermo_profile.md)
- [FROR_electro_profile](./FROR_electro_profile.md)
- [FROR_relativity_profile](./FROR_relativity_profile.md)
- [FROR_hilbert_profile](./FROR_hilbert_profile.md)
- [FROR_sm_profile](./FROR_sm_profile.md)
- [FROR_schrodinger_profile](./FROR_schrodinger_profile.md)
- [FROR_gravity_profile](./FROR_gravity_profile.md)
- [FROR_light_speed_profile](./FROR_light_speed_profile.md)
- [DomainMapping/fror/*](./DomainMapping/fror)
- [FROR_CDM_bridge](../cdm/bridge/FROR_CDM_bridge.md)

Что хранится:
- перевод канонических объектов в доменные термины;
- доменные наблюдаемые величины;
- bridge-правила совместимости слоёв.

Правило:
- profile не может переопределять Core/Criteria;
- profile может только конкретизировать измеримые операторы.

------------------------------------------------------------------------

## 4) Experiments (измерение и проверка)

Файлы:
- [FROR_class_measurement](./FROR_class_measurement.md)
- [FROR_GRAPH](./FROR_GRAPH.md)
- [FROR_SLOT_FORM](./FROR_SLOT_FORM.md)
- [FROR_ds3_attractor](./FROR_ds3_attractor.md)

Что хранится:
- экспериментальные протоколы;
- параметры генерации и измерителей;
- статистические критерии подтверждения/опровержения.

Правило:
- экспериментальные эвристики не имеют статуса канона до переноса в Core/Criteria.

------------------------------------------------------------------------

## 5) Протокол эскалации утверждений

Статусы:
1. `Conjecture` (гипотеза)
2. `Protocol` (есть воспроизводимый тест)
3. `Validated in profile` (подтверждено в конкретной нормализации)
4. `Canonical candidate` (кандидат в Criteria/Core)

Минимальные условия перехода вверх:
- явные допущения;
- воспроизводимый протокол;
- критерий фальсификации;
- отсутствие конфликта с действующим каноном.

------------------------------------------------------------------------

## 6) Краткая карта источников истины

- Время/необратимость: I3--I4 в [FROR_normalizations_invariants](./FROR_normalizations_invariants.md)
- Определения `c_fix`, `c_bg`, `τ`, `D`, `ΔI_miss`: D4/D4b/D5/D5b/D8 в [FROR_axioms_v0_2](./FROR_axioms_v0_2.md)
- Трихотомия и порог `R >= 3`: A3/T2 в [FROR_axioms_v0_2](./FROR_axioms_v0_2.md)
- Порог памяти для нетривиальной симметрии: [FROR_symmetry_memory_threshold](./FROR_symmetry_memory_threshold.md)
- Доменные rollback-правила: [FROR_DomainLexicon](./FROR_DomainLexicon.md) и [FROR_CDM_bridge](../cdm/bridge/FROR_CDM_bridge.md)

------------------------------------------------------------------------

## 7) Практическое правило редактирования

Перед добавлением нового тезиса:
1. Определить слой (`Core/Criteria/Profiles/Experiments`);
2. Проверить, не дублирует ли он существующий источник истины;
3. Если это дублирование, оставить короткую ссылку на канонический файл;
4. Если это новый тезис, добавить допущения и фальсификацию.
