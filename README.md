# fcdm-core

Теоретическое ядро стека:

`FROR -> CDM -> bridge`

Здесь находится не operational delivery-слой и не tool-integration слой, а
инвариантный теоретический контур, из которого далее строятся:

1. `CDM` как каноническая логика исполнения изменения;
2. bridge-слои между `FROR` и `CDM`;
3. прикладные operational/methodology слои вне этого репозитория, включая
   `MMCF`.

## Что это такое

`fcdm-core` хранит:

1. `FROR` как фундаментальный слой инвариантов ресурса различения, фиксации,
   цены и эффективной необратимости;
2. `CDM` как каноническую морфологию `LifeCycle`, `ChangeFlow`,
   `PhaseTransition`, `Context` и связанных сущностей;
3. bridge-документы, показывающие, как инварианты `FROR` реализуются в
   канонической логике `CDM`.

Короткая рабочая формула:

- `FROR` отвечает на вопрос: какие инварианты должны сохраняться;
- `CDM` отвечает на вопрос: как эти инварианты исполняются в каноническом
  цикле изменения;
- `MMCF` и иные applied-слои строятся уже поверх этого основания.

## Что это не такое

`fcdm-core` не является:

1. готовой operational-методикой внедрения;
2. заменой `Scrum`, `Agile`, `Kanban`, `Linear` и других внешних систем;
3. исполняемым runtime-контуром;
4. завершенной доказанной научной теорией во всех его ветвях сразу.

Корректнее читать корпус как:

1. инвариантный теоретический каркас;
2. исследовательскую программу с разной зрелостью утверждений;
3. площадку для междоменной проверки, критики и калибровки.

## Границы репозитория

Разрешено:

1. теория;
2. канон;
3. доменные примеры как иллюстрации и проверки переносимости паттернов модели;
4. claim-maturity, protocol contours и experiment registries;
5. bridge-документы между слоями.

Не должны жить здесь как source of truth:

1. `ICSS`;
2. parser/runtime;
3. SQL/materialization;
4. delivery/tool-integration профили;
5. исполняемый product/application слой.

## Как читать корпус

### 1. Если нужен фундамент

Начните с:

- [FROR index](./theory/fror/FROR_INDEX.md)
- [FROR theory status and validation stance](./theory/fror/FROR_THEORY_STATUS_AND_VALIDATION_STANCE.md)
- [FROR architecture](./theory/fror/FROR_architecture_v2.md)
- [FROR main](./theory/fror/FROR_main.md)

### 2. Если нужен канонический слой изменения

Дальше переходите к:

- [CDM canonical specifications](./theory/cdm/Specifications)
- [FROR <-> CDM bridge](./theory/cdm/bridge/FROR_CDM_bridge.md)

### 3. Если нужен applied-layer

Operational governance и delivery находятся уже вне `fcdm-core`, в соседнем
корпусе `mmcf-docs`.

## Статус теории

Наиболее важное различение для чтения репозитория:

1. не все файлы имеют одинаковую зрелость;
2. `Core`, `Criteria`, `Profiles`, `Experiments` и `Overview` не должны
   смешиваться;
3. `Conjecture`, `Protocol`, `Validated`, `Core` — это не декоративные
   статусы, а рабочая дисциплина корпуса.

Особенно для `FROR`:

- центральный инвариантный тезис строится вокруг конечного ресурса
  различения, неинъективной фиксации и эффективной необратимости;
- более сильные контуры (`3+1`, quantum-like profiles, agency profiles и т.д.)
  должны читаться только в своей maturity-рамке;
- междоменная переносимость является не риторикой, а отдельным объектом
  проверки.

Подробно это разложено в:

- [FROR theory status and validation stance](./theory/fror/FROR_THEORY_STATUS_AND_VALIDATION_STANCE.md)

## Главные входные точки

- [FROR index](./theory/fror/FROR_INDEX.md)
- [FROR architecture](./theory/fror/FROR_architecture_v2.md)
- [FROR claims workflow](./theory/fror/FROR_claims_git_workflow.md)
- [FROR experiment registry](./theory/fror/FROR_experiment_registry.md)
- [FROR DomainLexicon](./theory/fror/FROR_DomainLexicon.md)
- [FROR <-> CDM bridge](./theory/cdm/bridge/FROR_CDM_bridge.md)

## Техническое примечание

Для FROR claim-checker и git hooks нужен `PyYAML`
(`python3 -m pip install --user PyYAML`).
