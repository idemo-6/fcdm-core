---
title: "Профиль: Identity Scoring (прикладной)"
date: 2026-03-01
tags: [CDM, Identity, profile, scoring]
citekey: cdm_identity_scoring_profile_ru_2026
---

# Профиль: Identity Scoring (прикладной)

## 1. Назначение

Профиль задает операционную оценку сохранения идентичности поверх канона `Identity`.

---

## 2. Нормативная граница

Это профиль, а не канон.

Опорные документы:
- `Identity (каноническая)`
- `System (каноническая)`
- `LifeCycle-6 (каноническая)`
- `PhaseTransition (каноническая)`

---

## 3. Базовая структура оценки

Профильный вектор:

`IdBasis = <R, F, C, T>`

где:
- `R` — правила/ограничения;
- `F` — фазово-функциональная сигнатура LC/CF;
- `C` — контекстная связность;
- `T` — временная непрерывность.

---

## 4. Профильная формула (пример)

`IdScore(S -> S') = gamma * (w_r*sim(R,R') + w_f*sim(F,F') + w_c*sim(C,C') + w_t*sim_t(T,T'))`

`gamma = max(0, 1 - Delta_t_gap / epsilon_class)`

где:
- `sim(*)` — доменно-выбранная метрика сходства (например, Jaccard);
- `sim_t(*)` — метрика непрерывности временной связности;
- `w_r + w_f + w_c + w_t = 1`;
- `epsilon_class` и `theta_class` задаются профильной политикой.

Решение:
- `IdScore >= theta_class` -> `transform` (идентичность сохранена),
- `IdScore < theta_class` -> `death + birth`.

При недостаточной полноте наблюдений:
- `evidence_completeness < tau_evidence` -> `identity_underdetermined` (без принудительного бинарного вывода).

---

## 5. Ограничения профиля

1. Пороги и веса не универсальны, а доменно-калибруемые.
2. Формула не должна переопределять инварианты канона.
3. Для спорных случаев требуется трассируемое объяснение вклада `R/F/C/T`.
4. Профиль обязан явно задавать `tau_evidence` и правило вычисления `evidence_completeness`.

---

## 6. Минимальная трасса для evaluate

Для каждого решения по идентичности фиксировать минимум:
- `id_basis_snapshot_before` / `id_basis_snapshot_after`;
- `weights` (`w_r,w_f,w_c,w_t`);
- `epsilon_class`, `theta_class`, `tau_evidence`;
- `delta_t_gap`, `gamma`, частные сходства `sim_*`;
- итоговый `IdScore`;
- итоговое решение (`identity_preserved | identity_broken | identity_underdetermined`).

---

## 7. Миграция legacy-содержания

Допускается перенос legacy-таблиц (`epsilon_class`, `theta_class`, `w_*`) в приложение к этому профилю как стартовые значения калибровки, а не как канонические константы.

---

## 8. Заключение

Identity Scoring профиль превращает каноническую проверку идентичности в практическую процедуру принятия решений без изменения онтологии CDM.

---

## Appendix A. Initial calibration (legacy import, non-canonical)

Назначение:
- стартовые значения для первичной настройки профиля;
- источник: legacy identity tables (pre-CDM, версия 1.3.10);
- статус: **рекомендательные**, не канонические.

Правила применения:
1. Использовать только как bootstrap до доменной калибровки.
2. Фиксировать версию набора коэффициентов в trace.
3. Пересматривать на эмпирических данных при изменении контура наблюдения.

### A1. Начальные веса и пороги по классам

| Класс системы | w_r | w_f | w_c | w_t | epsilon_class | theta_class |
|---|---:|---:|---:|---:|---|---:|
| C1 (deterministic) | 0.45 | 0.35 | 0.10 | 0.10 | 10^6 years | 0.75 |
| C2 (bio/autonomous) | 0.35 | 0.25 | 0.25 | 0.15 | 1 second | 0.65 |
| C3 (collective) | 0.30 | 0.25 | 0.30 | 0.15 | 1 minute | 0.65 |
| C4 (ind-mind-I) | 0.25 | 0.20 | 0.35 | 0.20 | 1 hour | 0.60 |
| C5 (ind-mind-II) | 0.20 | 0.20 | 0.35 | 0.25 | 1 day | 0.55 |
| C6 (meta/supersystem) | 0.15 | 0.20 | 0.35 | 0.30 | domain-defined | domain-defined |

Ограничения таблицы:
1. Для каждой строки должно выполняться: `w_r + w_f + w_c + w_t = 1`.
2. Значения `epsilon_class` и `theta_class` валидны только в рамках выбранного контура наблюдения.
3. Для `C6` пороги задаются доменным governance-профилем.

### A2. Метаморфозы (guideline)

Кейс типа `metamorphosis` (например, `caterpillar -> butterfly`) допускает `identity_preserved`, если:
1. сохраняется базовый инвариантный каркас `R`;
2. сохраняется допустимая фазовая сигнатура `F`;
3. подтверждена операционная непрерывность `T`.

Рекомендация:
- для таких кейсов задавать понижающий коэффициент доверия к структурному сходству (`sim(R,R')`), но не форсировать `identity_broken` автоматически.

### A3. Минимальный trace для calibration-run

В calibration-run дополнительно фиксировать:
1. `calibration_profile_id`;
2. `class_tag`;
3. `weights_source = legacy_initial`;
4. `evidence_completeness`;
5. решение о принятии/отклонении стартовых весов после валидации.

---

## Appendix B. Reference calibration scenarios

Назначение:
- быстрый smoke-check профиля;
- проверка согласованности решения и trace-полей.

Формат сценария:
1. `Scenario ID`
2. `Class`
3. `Input summary`
4. `Expected decision`
5. `Trace minimum`

### B1. Stable continuation (C1)

1. `Scenario ID`: `ID-CAL-001`
2. `Class`: `C1`
3. `Input summary`:
- `sim(R,R')=0.95`, `sim(F,F')=0.92`, `sim(C,C')=0.80`, `sim_t(T,T')=0.98`
- `Delta_t_gap << epsilon_class`
- `evidence_completeness >= tau_evidence`
4. `Expected decision`: `identity_preserved`
5. `Trace minimum`:
- `IdScore >= theta_class`
- все `sim_*` и `gamma` зафиксированы

### B2. Hard break (C2)

1. `Scenario ID`: `ID-CAL-002`
2. `Class`: `C2`
3. `Input summary`:
- резкое падение `sim(F,F')` и `sim(C,C')` (ниже доменных допустимых границ)
- `Delta_t_gap` близок к `epsilon_class` или выше
- `evidence_completeness >= tau_evidence`
4. `Expected decision`: `identity_broken`
5. `Trace minimum`:
- `IdScore < theta_class`
- явно зафиксированы факторы, давшие основной вклад в разрыв

### B3. Metamorphosis-like continuity (C2)

1. `Scenario ID`: `ID-CAL-003`
2. `Class`: `C2`
3. `Input summary`:
- `sim(R,R')` умеренно снижен из-за структурной перестройки
- `sim(F,F')` и `sim_t(T,T')` остаются высокими
- контекстная связность сохранена
- `evidence_completeness >= tau_evidence`
4. `Expected decision`: `identity_preserved`
5. `Trace minimum`:
- отдельная пометка `metamorphosis_case=true`
- обоснование, почему снижение `sim(R,R')` не привело к `identity_broken`

### B4. Underdetermined evidence (C4)

1. `Scenario ID`: `ID-CAL-004`
2. `Class`: `C4`
3. `Input summary`:
- часть обязательных наблюдений отсутствует
- `evidence_completeness < tau_evidence`
- частные `sim_*` неустойчивы/неполны
4. `Expected decision`: `identity_underdetermined`
5. `Trace minimum`:
- зафиксирован `tau_evidence`
- перечислены отсутствующие наблюдения
- отсутствует форсированный бинарный вывод

### B5. Borderline threshold (C5)

1. `Scenario ID`: `ID-CAL-005`
2. `Class`: `C5`
3. `Input summary`:
- `IdScore` находится в окрестности `theta_class` (пограничный случай)
- `evidence_completeness >= tau_evidence`
- высокая чувствительность к весам `w_*`
4. `Expected decision`: допускается `identity_preserved` или `identity_broken` по доменной политике tie-break
5. `Trace minimum`:
- зафиксирован policy tie-break rule
- сохранены альтернативные вычисления (`sensitivity snapshot`)
- обоснование выбора финального решения
