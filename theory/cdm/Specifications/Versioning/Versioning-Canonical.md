---
title: "CDM Profile: Versioning (state-derived)"
date: 2026-03-01
tags: [CDM, versioning, profile, lifecycle, changeflow]
citekey: cdm_versioning_profile_ru_2026
---

# CDM Profile: Versioning (state-derived)

> Документ задает **канонический CDM-профиль** state-derived versioning для
> сущностей, проходящих `LifeCycle` и `ChangeFlow`. MMCF может использовать
> этот профиль как governance/application mapping, но не задает первичный
> source of truth для версии.

---

## 1. Область определения

Документ задает профильную схему версионирования сущностей CDM:

- для документов (`doc:*`);
- для систем (`sys:*`);
- для любых доменных сущностей, проходящих `LifeCycle` и `ChangeFlow`.

Версия вычисляется как функция подтвержденных фазовых переходов и не
задается вручную.

---

## 2. Нормативные ссылки

- [MMCF Versioning Governance Profile](../../../../../mmcf-docs/methodology/Versioning-Canonical.md)
- [[fcdm-core/theory/cdm/Specifications/LifeCycle-6_v2|LifeCycle-6]]
- [[fcdm-core/theory/cdm/Specifications/ChangeFlow-6_v3|ChangeFlow-6]]
- [[fcdm-core/theory/cdm/Specifications/PhaseTransition_Specifications/PhaseTransition_Overview|PhaseTransition Overview]]
- [[fcdm-core/theory/cdm/Specifications/PhaseTransition_Specifications/PhaseTransition-LC|PhaseTransition-LC]]
- [[fcdm-core/theory/cdm/Specifications/PhaseTransition_Specifications/PhaseTransition-CF|PhaseTransition-CF]]
- [[fcdm-core/theory/cdm/Specifications/System/Identity-Canonical|Identity Canonical]]
- [[fcdm-core/theory/cdm/Specifications/Claim-Maturity-Profile|Claim-Maturity-Profile]]

---

## 3. Идентификатор сущности (EntityId)

### 3.1 Принцип

Версия всегда привязана к неизменяемому идентификатору сущности:

`EntityVersion = EntityId @ VersionState`

где:

- `EntityId` — постоянный id сущности;
- `VersionState` — состояние сущности в координатах LC/CF.

### 3.2 Форматы без сквозной нумерации

Допускаются канонические форматы:

- `doc:<space>/<slug>#<hash8>`
- `sys:<domain>/<name>#<hash8>`

Примеры:

- `doc:core/lifecycle-6-canonical#A17F9C2B`
- `sys:idemo/cdm#5D0E21AA`

`hash8` регистрируется при создании сущности и далее не пересчитывается.

---

## 4. Каноническая структура версии

### 4.1 VersionState

Каноническая форма:

`VersionState = v.<inc>.<lc>.<cf>.<cfp>`

где:

- `inc` — индекс инкарнации (transform-уровень);
- `lc` — индекс текущей фазы LifeCycle;
- `cf` — индекс текущего осмысленного ChangeFlow;
- `cfp` — индекс текущей фазы ChangeFlow.

Полная версия:

`EntityVersion = <EntityId>@v.<inc>.<lc>.<cf>.<cfp>`

### 4.2 Индексы фаз

Для `lc`:

- `1 -> F1`
- `2 -> F2`
- `3 -> F3`
- `4 -> F4`
- `5 -> F5`
- `6 -> F6`

Для `cfp`:

- `1 -> collect`
- `2 -> analyze`
- `3 -> forecast`
- `4 -> decide`
- `5 -> implement`
- `6 -> evaluate`

---

## 5. Канонические правила инкремента

1. `inc` увеличивается только при подтвержденном `transform`:
- завершение предыдущего LC;
- запуск новой инкарнации с сохранением идентичности.

2. `lc` меняется только по подтвержденному `LC.PhaseEnter(Fi, t)`.

3. `cf` считается по осмысленным task-scoped ChangeFlow:
- обязательны `intent_ref` и `task_ref`;
- `commit_refs` являются трассой реализации, но не заменяют `cf`.

4. `cfp` меняется только по подтвержденному `CF.PhaseEnter(...)`.

5. Ручное изменение `VersionState` запрещено.
Исключение: аварийный override с обязательным audit trail.

---

## 6. Инварианты

1. `EntityId` неизменяем в пределах всех инкарнаций сущности.
2. Одинаковый event log -> одинаковая версия (детерминизм).
3. Любой компонент версии должен иметь доказуемое событие-основание.
4. Технические коммиты вне task-scoped CF не изменяют `cf`.

---

## 7. Связь с SemVer

`SemVer` допускается как внешний release-label.

Профильное CDM-versioning:

- не заменяется `SemVer`;
- описывает состояние сущности во времени (`LC + CF`);
- используется как источник аудита и трассируемости.

---

## 7b. Связь со статусами зрелости утверждений

`ClaimStatus` (`Conjecture/Protocol/Validated/Core`) не является частью
`VersionState` и не включается в `v.<inc>.<lc>.<cf>.<cfp>`.

Иными словами:
- `EntityVersion` отвечает на вопрос "в каком процессном состоянии сущность";
- `ClaimStatus` отвечает на вопрос "какова зрелость конкретного тезиса".

Правила и гейты claim-статусов задаются в:
- [[fcdm-core/theory/cdm/Specifications/Claim-Maturity-Profile|Claim-Maturity-Profile]]

---

## 8. Минимальный машинный контракт

Для вычисления версии необходимы события:

- `Entity.Created(entity_id, t0)`
- `LC.Start(entity_id, inc, t)`
- `LC.PhaseEnter(entity_id, Fi, t)`
- `CF.Start(entity_id, cf_id, intent_ref, task_ref, t)`
- `CF.PhaseEnter(entity_id, cf_id, phase, t)`
- `CF.End(entity_id, cf_id, result, t)`
- `LC.End(entity_id, mode, t)` (`mode in {end, transform}`)

Подробная процедура вычисления:

- [[fcdm-core/theory/cdm/Specifications/Versioning/Version-Derivation-Policy|Version-Derivation-Policy]]
