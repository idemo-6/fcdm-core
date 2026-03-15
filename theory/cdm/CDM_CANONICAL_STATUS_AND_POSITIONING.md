# CDM Canonical Status And Positioning

Этот файл нужен, чтобы коротко зафиксировать правильное место `CDM` в общем
корпусе.

## 1. Короткая позиция

`CDM` следует читать как канонический execution layer.

То есть:

1. не как альтернативу `FROR`;
2. не как прикладную operational methodology;
3. не как UI/tool profile;
4. а как каноническую процессную логику, через которую materialize'ятся
   инварианты `FROR`.

## 2. Роль `CDM` в вертикали

Рабочая вертикаль корпуса:

1. `FROR` — инварианты ресурса различения, фиксации, цены, rollback deficit,
   effective irreversibility;
2. `CDM` — канонические формы исполнения изменения;
3. `MMCF` — прикладной governance / operational layer;
4. delivery/tool profiles — внешние operational systems of realization.

Следовательно, `CDM` отвечает не на вопрос “какая методика лучше”, а на
вопрос:

как должен быть устроен канонический цикл изменения, если инварианты уже
заданы.

## 3. Что составляет ядро `CDM`

Наиболее важные канонические сущности:

1. `LifeCycle`
2. `ChangeFlow`
3. `PhaseTransition`
4. `Intent`
5. `Context`
6. `Experience`
7. `System`

Это и есть минимальный канонический каркас `CDM`.

## 4. Что `CDM` не должен подменять

`CDM` не должен подменять:

1. инварианты `FROR`;
2. domain lexicon;
3. tool-specific profiles;
4. delivery governance;
5. team rituals.

Он также не должен смешиваться с:

1. DSL aliases;
2. parser/runtime contracts;
3. applied management overlays.

## 5. Главный смысл `CDM`

Если сформулировать совсем коротко, `CDM` нужен для того, чтобы:

1. задать каноническую морфологию изменения;
2. развести режим существования системы и атомарный акт изменения;
3. удержать самостоятельность переходов (`PhaseTransition`);
4. сделать `Intent`, `Context` и `Result` частью строгого канона, а не
   только прикладной интерпретации.

## 6. Как правильно читать его связь с `FROR`

Наиболее корректная формула:

- `FROR` задает, что обязано сохраняться;
- `CDM` задает, как это реализуется в канонической логике.

То есть `CDM` не спорит с `FROR`, а operationally-canonically разворачивает
его на уровне жизненного цикла, акта изменения, контекста и результата.

## 7. Как правильно читать его связь с `MMCF`

Наиболее корректная формула:

- `CDM` — канон;
- `MMCF` — applied layer.

Поэтому:

1. `MMCF` не должен менять `CDM` под tool constraints;
2. `MMCF` должен materialize'ить `CDM` в реальных рабочих системах;
3. delivery-профили следует читать как внешние проекции канонического слоя.

## 8. Почему это важно для входного слоя

Без этой рамки новый читатель легко путает:

1. `FROR`-инварианты;
2. `CDM`-канон;
3. `MMCF`-методологию;
4. delivery/tool mappings.

Правильный вход в `CDM` должен снимать эту путаницу заранее.

## 9. Рекомендуемый порядок чтения

1. [FROR <-> CDM bridge](./bridge/FROR_CDM_bridge.md)
2. [LifeCycle-6](./Specifications/LifeCycle-6_v2.md)
3. [ChangeFlow-6](./Specifications/ChangeFlow-6_v3.md)
4. [Intent](./Specifications/Intent-1.1.5.md)
5. [Context Canonical](./Specifications/Context/Context-Canonical.md)
6. [System Canonical](./Specifications/System/System-Canonical.md)
