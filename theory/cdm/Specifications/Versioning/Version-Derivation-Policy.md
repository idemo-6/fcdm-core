---
title: "CDM Policy: Version Derivation from Event Log"
date: 2026-03-01
tags: [CDM, versioning, profile-policy, event-log, derivation]
citekey: cdm_version_derivation_profile_policy_ru_2026
---

# CDM Policy: Version Derivation from Event Log

## 1. Назначение

Документ задает детерминированную процедуру вычисления:

`EntityVersion = <EntityId>@v.<inc>.<lc>.<cf>.<cfp>`

на основании верифицированного event log.

Нормативная база:

- [[fcdm-core/theory/cdm/Specifications/Versioning/Versioning-Canonical|Versioning-Canonical]]
- [MMCF Versioning Governance Profile](../../../../../mmcf-docs/methodology/Versioning-Canonical.md)

---

## 2. Требования к журналу событий

Каждое событие должно содержать минимум:

- `event_id` (уникальный);
- `entity_id`;
- `event_type`;
- `timestamp` (UTC, монотонная упорядочиваемость);
- `actor`;
- `evidence_refs` (опционально для технических событий, обязательно для gate-событий).

Для CF-событий обязательны:

- `cf_id`;
- `intent_ref`;
- `task_ref`.

---

## 3. Учет осмысленного ChangeFlow

CF включается в индекс `cf`, если выполнены условия:

1. Есть `CF.Start` с заполненными `intent_ref`, `task_ref`.
2. CF прошел минимум до `CF.PhaseEnter(collect, ...)`.
3. Существует связанная реализационная трасса (`commit_refs` в CF-метаданных или эквивалентный linkage).

Коммиты без CF-контекста в индекс `cf` не входят.

---

## 4. Алгоритм вычисления

1. Отфильтровать события по `entity_id`.
2. Проверить целостность последовательности:
- нет дубликатов `event_id`;
- нет обратных переходов фаз;
- LC/CF переходы соответствуют PhaseTransition-правилам.
3. Определить текущую инкарнацию `inc`:
- `inc = 1` на первом `LC.Start`;
- `inc = inc + 1` после `LC.End(mode=transform)` и следующего `LC.Start`.
4. Определить `lc`:
- индекс последнего валидного `LC.PhaseEnter(Fi, ...)`.
5. Определить `cf`:
- порядковый номер текущего/последнего валидного task-scoped CF в текущей инкарнации.
6. Определить `cfp`:
- индекс последнего валидного `CF.PhaseEnter(...)` для текущего `cf`.
7. Сформировать:
- `<EntityId>@v.<inc>.<lc>.<cf>.<cfp>`.

---

## 5. Правила сброса и продолжения

1. При новой инкарнации (`inc + 1`) индекс `cf` начинается с `1`.
2. При новом CF в той же инкарнации:
- `cf = cf + 1`,
- `cfp = 1` после входа в `collect`.
3. При `CF.End` без старта следующего CF версия сохраняет последний `cf`/`cfp`.

---

## 6. Gate-валидация переходов

Каждый фазовый переход учитывается в версии только при наличии:

- валидного transition-события;
- выполненных гейтов/метрик согласно:
  - [[fcdm-core/theory/cdm/Specifications/PhaseTransition_Specifications/PhaseTransition-LC|PhaseTransition-LC]]
  - [[fcdm-core/theory/cdm/Specifications/PhaseTransition_Specifications/PhaseTransition-CF|PhaseTransition-CF]]

События без подтвержденного gate не изменяют версию.

---

## 7. Псевдокод

```text
derive(entity_id, log):
  events = normalize_and_sort(log, entity_id)
  assert validate_integrity(events)

  inc = current_incarnation(events)
  lc  = current_lc_phase_index(events)
  cf  = current_meaningful_cf_index(events, inc)
  cfp = current_cf_phase_index(events, inc, cf)

  return entity_id + "@v." + inc + "." + lc + "." + cf + "." + cfp
```

---

## 8. Аудит и override

Ручной override версии допустим только в аварийном режиме и обязан иметь:

- `override_reason`;
- `approved_by`;
- `approved_at`;
- `replay_plan` (как восстановить состояние из журнала).

Override не отменяет требование последующей нормализации и re-derivation.
