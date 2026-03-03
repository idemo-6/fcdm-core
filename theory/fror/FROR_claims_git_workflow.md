# FROR Claims: User Workflow (Registry, Event Log, Git Hooks)

## 1. Цель

Документ описывает полный рабочий цикл зрелости утверждений FROR:
- где живёт текущее состояние claim;
- как фиксируются переходы статусов;
- как это валидируется;
- как git-хуки предотвращают неаудируемые изменения.

Принцип: **версия документа** и **зрелость утверждения** независимы.

## 2. Артефакты и роли

### 2.1 Реестр текущего состояния

Файл: `theory/fror/claims_registry.yaml`

Назначение:
- хранит текущий статус каждого claim;
- хранит минимальный паспорт тезиса (`claim_id`, statement, assumptions, falsification, evidence_refs).

Это "срез состояния", удобный для чтения людьми.

### 2.2 Журнал событий

Файл: `theory/fror/claim_event_log.yaml`

Назначение:
- хранит историю переходов (`Claim.Created`, `Claim.ProtocolAttached`, `Claim.Validated`, `Claim.CoreAccepted`, `Claim.Override`);
- задаёт аудируемую траекторию зрелости claim.

Это "журнал изменений", источник происхождения статуса.

### 2.3 Валидация согласованности

Файл: `theory/fror/check_claim_status_transitions.py`

Проверяет:
- корректность последовательности статусов;
- отсутствие запрещённых переходов назад и через ступень;
- совпадение итогового статуса из журнала с `claims_registry.yaml`;
- отсутствие "лишних" claim в журнале.

## 3. Каноническая шкала статусов

Статусы:
1. `Conjecture`
2. `Protocol`
3. `Validated`
4. `Core`

Разрешённый переход:
- только на следующую ступень (`Conjecture -> Protocol -> Validated -> Core`);
- обратные переходы и skip-level запрещены (кроме отдельного event-type `Claim.Override`).

## 4. Git-интеграция

### 4.1 Хуки

Папка: `.githooks`

Хуки:
- `pre-commit`: запускает `check_claim_status_transitions.py`;
- `commit-msg`: если изменены `claims_registry.yaml` или `claim_event_log.yaml`, требует маркер `claim: FROR-CLM-XXX` в тексте коммита;
- `pre-push`: повторно запускает проверку перед `push`.

### 4.2 Установка хуков

Один раз в локальном репозитории:

```bash
cd fcdm-core
bash scripts/install-git-hooks.sh
```

Скрипт:
- выставляет `+x` для хуков;
- включает `core.hooksPath=.githooks`.

Проверка установки:

```bash
git config --get core.hooksPath
```

Ожидаемое значение: `.githooks`.

## 5. Повседневный workflow для автора

### Шаг 1. Создание claim

1. Добавить запись в `claims_registry.yaml` со статусом `Conjecture`.
2. Добавить событие `Claim.Created` в `claim_event_log.yaml`.

### Шаг 2. Поднятие до Protocol

1. Добавить/обновить протокол в FROR-документах.
2. Добавить событие `Claim.ProtocolAttached`.
3. Обновить `status: Protocol` в `claims_registry.yaml`.

### Шаг 3. Поднятие до Validated

1. Добавить evidence по протоколу.
2. Добавить событие `Claim.Validated`.
3. Обновить `status: Validated`.

### Шаг 4. Поднятие до Core

1. Проверить конфликт с действующим Core/Criteria.
2. Добавить событие `Claim.CoreAccepted`.
3. Обновить `status: Core`.

### Шаг 5. Коммит

Коммит должен содержать маркер claim, если менялись файлы статусов:

```text
docs(fror): promote irreversibility claim

claim: FROR-CLM-002
```

Если маркера нет, `commit-msg` hook отклонит коммит.

## 6. Команды проверки

Локальная ручная проверка:

```bash
cd fcdm-core/theory/fror
python3 check_claim_status_transitions.py
```

Ожидаемый success:

```text
OK
validated_claims=<N>
```

## 7. Политика override

`Claim.Override` допустим только как исключение:
- с явной причиной;
- с планом повторной валидации;
- с последующим возвратом к state-derived статусу.

Практика: использовать override редко и явно документировать в event log.

## 8. Что это даёт

- Аудируемость: видно, **когда и почему** claim сменил статус.
- Воспроизводимость: один и тот же журнал даёт один и тот же итоговый статус.
- Защита от "ручных скачков": хуки и checker ловят несогласованные правки до push.
- Чёткая граница между зрелостью знания и редакторской версией файла.
