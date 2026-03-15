# FROR / Lambda-Phy: second-law-like profile

## 0. Статус

- Слой: `Profiles / Conjectural program`.
- Это не `Core` и не доказанный канонический вывод `FROR`.
- Файл задает возможное вычислительное чтение observer-level arrow и
  second-law-like behavior через язык ветвления вычислительных траекторий,
  конечной памяти и coarse-graining.

Корректное чтение:

1. это не доказательство всей термодинамики;
2. это не автоматическое следствие `A1..A5` без дополнительных предпосылок;
3. это conjectural profile, который должен оцениваться через отдельные
   assumptions, protocols и non-support criteria.

Сильнейший связанный claim в current corpus:

- `FROR-CLM-012` in [FROR_experiment_registry](./FROR_experiment_registry.md)

## 1. Назначение

Этот файл предлагает profile-level reading, в котором:

1. ветвление вычислительных траекторий;
2. конечный ресурс различения наблюдателя;
3. неинъективный coarse-graining;
4. цена фиксации и восстановления различий

могут приводить к second-law-like росту наблюдаемой дефектной энтропии.

То есть речь идет не о прямом выводе классической термодинамики из одного
формализма, а о conjectural computational contour для `FROR`-совместимого
чтения observer-level arrow.

## 2. Связанные документы

- [FROR_architecture_v2](./FROR_architecture_v2.md)
- [FROR_axioms_v0_2](./FROR_axioms_v0_2.md)
- [FROR_main](./FROR_main.md)
- [FROR_normalizations_invariants](./FROR_normalizations_invariants.md)
- [FROR_experiment_registry](./FROR_experiment_registry.md)
- [FROR_THEORY_STATUS_AND_VALIDATION_STANCE](./FROR_THEORY_STATUS_AND_VALIDATION_STANCE.md)

## 3. Working hypothesis

Рабочая гипотеза профиля:

1. если вычислительная динамика имеет множество альтернативных ветвей;
2. а наблюдатель конечен по памяти, вычислительному бюджету и стратегии
   различения;
3. то он не способен удерживать все альтернативы по отдельности;
4. возникает coarse-graining классов траекторий;
5. точное восстановление истории становится ресурсно дорогим;
6. наблюдаемая стрела и second-law-like рост дефектной энтропии могут
   возникать как эффективный, а не фундаментально аксиоматический режим.

Это согласуется с каноническим ядром `FROR`, но не тождественно ему.

## 4. Профильная вычислительная постановка

В качестве conjectural normalizing language вводится:

1. `PrimeMover` — замкнутый `lambda`-term, представляющий глобальную систему;
2. последовательность `beta`-редукций как одна из возможных моделей
   микродинамики;
3. `Omega(Sigma)` как множество достижимых состояний на данном шаге;
4. наблюдатель с конечной памятью и coarse-graining strategy.

Важно:

1. `lambda`-язык здесь является profile-level носителем;
2. он не вводится как фундаментальная онтология всего `FROR`;
3. этот контур нужно читать как возможную вычислительную нормализацию,
   а не как канонический единственный язык ядра.

## 5. Наблюдатель и coarse-graining

Профиль использует наблюдателя вида:

`O = (M_O, Sigma_O, pi_O)`

где:

1. `M_O` — конечная память;
2. `Sigma_O` — доступный вычислительный бюджет;
3. `pi_O` — стратегия coarse-graining.

Если число альтернативных траекторий превышает различительную способность
наблюдателя, он переходит от отдельных ветвей к классам эквивалентности.

Именно это profile-level чтение связывает:

1. ветвление траекторий;
2. потерю различимости;
3. запись outcome class;
4. effective irreversibility.

## 6. Second-law-like reading

В этом профиле допускается ввод величины:

`S_defect ~ ln Omega_reachable`

как меры числа физически/операционно достижимых классов состояний в выбранной
нормализации.

Дальше формулируется conjectural reading:

1. если восстановление точного прошлого требует удержания или реконструкции
   недоступных ветвей;
2. а ресурсы наблюдателя конечны;
3. то для physically realizable observer processes second-law-like arrow
   может проявляться как неубывание наблюдаемой defect entropy.

Корректная формула профиля:

- не "второй закон уже строго выведен";
- а "в данной вычислительной нормализации second-law-like growth является
  candidate consequence of finite distinguishability and branch compression".

## 7. Связь с FROR

Профиль опирается на уже существующие канонические идеи:

1. конечность ресурса различения;
2. неинъективная фиксация;
3. дефицит различимости;
4. эффективная необратимость;
5. различие между `tau` и внешним калибровочным временем.

Но профиль добавляет собственные предпосылки:

1. конкретный вычислительный carrier (`lambda`-style reduction);
2. специальную меру reachable classes;
3. особое чтение defect entropy;
4. особую вычислительную формулировку rollback-cost.

Поэтому он не должен читаться как прямой канонический файл ядра.

## 8. Что профиль не утверждает

Профиль не утверждает:

1. что классическая термодинамика уже выведена из `FROR`;
2. что `lambda`-исчисление является фундаментальной онтологией природы;
3. что любой рост наблюдаемой энтропии исчерпывается этим contour;
4. что все детали второго закона уже имеют protocol-level confirmation.

## 9. Что нужно для усиления этого профиля

Для перехода от narrative conjecture к protocol-level ветке нужно:

1. явно нормализовать carrier assumptions;
2. зафиксировать measure/observable для `S_defect`;
3. задать reproducible rollback-cost protocol;
4. описать support / non-support criteria;
5. связать результаты с `FROR-CLM-012`, а не существовать отдельно от
   claim-maturity machinery.

## 10. Короткая формулировка

Этот файл следует читать как conjectural profile:

`finite distinguishability + branch compression + rollback-cost`

`->`

`second-law-like observer-level arrow in a computational normalization`

а не как уже завершенный канонический вывод термодинамики из `FROR`.
