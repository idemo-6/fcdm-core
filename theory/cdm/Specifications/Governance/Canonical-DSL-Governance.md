---
title: "Governance: Canon <-> DSL Synchronization"
date: 2026-02-28
tags: [CDM, governance, canon, DSL, ICSS-IntentFlow]
citekey: cdm_governance_canon_dsl_ru_2026
---

# Governance: Canon <-> DSL Synchronization

## 1. Назначение

Документ фиксирует:
- что является source of truth;
- как синхронизируются канон CDM и машинный DSL-профиль ICSS-IntentFlow;
- какие изменения считаются допустимыми и как они принимаются.

---

## 2. Source of Truth

### 2.1 Онтологический канон (уровень смысла)

Source of truth для смысловой модели:
- `CDM/Specifications/LifeCycle-6_v2.md`
- `CDM/Specifications/ChangeFlow-6_v3.md`
- `CDM/Specifications/Intent-1.1.5.md`
- `CDM/Specifications/Context/Context-Canonical.md`
- `CDM/Specifications/CtxL/CtxL-Canonical.md`

При конфликте терминов/ролей между каноном и DSL приоритет всегда у канона.

### 2.2 Машинный профиль (уровень исполнения)

Source of truth для компиляции/валидации:
- `idemo-machine/docs/parser/spec_unified_v1.md`
- `idemo-machine/schemas/intent_ir_v1.json`
- `idemo-machine/tests/conformance/*`

Эти артефакты не меняют онтологию; они задают исполнимый профиль представления.

---

## 3. Контракт соответствия Canon <-> DSL

Обязательные инварианты:

1. Канонические фазы остаются `CF1..CF6`; DSL-маркеры (`@`, `??`, `~`, `^`, `>`, `_`) — только синтаксические алиасы.
2. `Result/Experience in {+1,0,-1}`; `0` трактуется как неприменимость (включая неопределенность как частный случай).
3. Один активный контекст на ветку выполнения.
4. `LC` задает доступность контекстов (`C_avail`), `C_coord` разрешает конфликты внутри доступного множества, `C_meta` управляет активацией и приоритетами контекстов.
5. `materialize(ctx)` допустима только для заранее объявленного контекста.

---

## 4. Процедура изменения (Change Process)

Каждое изменение относится к одному из типов:
- `C` (canonical): меняет смысловую онтологию;
- `P` (profile): меняет DSL/валидацию без изменения онтологии;
- `CP` (cross-plane): затрагивает и канон, и профиль.

### 4.1 Правила принятия

1. `C`-изменение требует обновления:
- минимум одного канонического документа;
- mapping-секции в `ChangeFlow-6_v3.md` (ICSS profile), если затронута исполнимая репрезентация.

2. `P`-изменение требует обновления:
- `idemo-machine/docs/parser/spec_unified_v1.md`;
- JSON Schema и/или conformance cases при изменении структуры/валидации.

3. `CP`-изменение принимается только при атомарной синхронизации:
- канон;
- профиль;
- conformance tests.

---

## 5. Release Gate (Definition of Done)

Изменение считается принятым только если выполнены все пункты:

1. Обновлены source-файлы нужного уровня (`C`, `P`, `CP`).
2. Не нарушены инварианты из раздела 3.
3. Для profile-изменений обновлены conformance cases.
4. В документах нет подмены канонических обозначений доменными/DSL-терминами.
5. Все новые формулы используют согласованную сигнатуру `Applicable(Intent, C_active, LC_phase)` (где применимо).

---

## 6. Версионирование

Рекомендуемая схема:
- `CDM Canon`: `canon.<major>.<minor>.<patch>`
- `ICSS Profile`: `icss.<major>.<minor>.<patch>`

Правила:
- `major`: несовместимое изменение;
- `minor`: расширение без нарушения совместимости;
- `patch`: редакционное/локальное исправление без изменения контракта.

---

## 7. Matrix синхронизации

Минимальная матрица проверки для каждого PR:

1. `Canonical docs` -> `ChangeFlow profile section` (алиасы фаз, инварианты).
2. `Context/Intent semantics` -> `idemo-machine/docs/parser/spec_unified_v1.md` (declared/use/materialize, result semantics).
3. `idemo-machine/docs/parser/spec_unified_v1.md` -> `idemo-machine/schemas/intent_ir_v1.json` (структурная совместимость).
4. `idemo-machine/docs/parser/spec_unified_v1.md` -> `idemo-machine/tests/conformance/*` (валидные/невалидные сценарии).

---

## 8. Статус

Документ является нормативным governance-контрактом для синхронизации CDM-канона и ICSS-IntentFlow профиля.
