# FROR: Quantum Protocol Contour

(сквозной protocol contour для quantum-like profile stack)

## Связанные заметки
- [FROR_architecture_v2](./FROR_architecture_v2.md)
- [FROR_axioms_v0_2](./FROR_axioms_v0_2.md)
- [FROR_main](./FROR_main.md)
- [FROR_hilbert_profile](./FROR_hilbert_profile.md)
- [FROR_Born_rule](./FROR_Born_rule.md)
- [FROR_measurement_profile](./FROR_measurement_profile.md)
- [FROR_schrodinger_profile](./FROR_schrodinger_profile.md)
- [FROR_dual_layer_profile](./FROR_dual_layer_profile.md)
- [FROR_experiment_registry](./FROR_experiment_registry.md)

------------------------------------------------------------------------

## 0. Статус

- Тип: `Protocol contour`.
- Это не `Core` и не самостоятельный `Claim`.
- Файл не повышает зрелость утверждений сам по себе.

Назначение:

- собрать quantum-like FROR stack в один воспроизводимый protocol contour;
- унифицировать assumptions, required artifacts, support criteria и
  non-support criteria;
- не дать профильным файлам дрейфовать в квази-канон.

------------------------------------------------------------------------

## 1. Глобальная оговорка

Этот файл не является доказательством квантовой механики.

Корректное чтение:

- FROR допускает набор quantum-like profile hypotheses;
- этот файл задаёт, как их проверять и чем их ограничивать;
- даже полная protocolization не равна подтверждению фундаментальной
  квантовой онтологии.

------------------------------------------------------------------------

## 2. Компоненты контура

Текущий quantum-like stack состоит из четырёх основных компонентов:

1. Hilbert-like amplitude encoding
2. Born-like probability rule
3. measurement-like fixation reading
4. Schrodinger-like reduced dynamics

Поддерживающий interpretive bridge:

5. dual-layer reading (`potential -> actual`)

------------------------------------------------------------------------

## 3. Роли файлов

| file | role |
|---|---|
| `FROR_hilbert_profile.md` | profile interpretation of amplitude encoding |
| `FROR_Born_rule.md` | profile interpretation of Born-like probability |
| `FROR_measurement_profile.md` | profile interpretation of fixation-as-measurement |
| `FROR_schrodinger_profile.md` | profile interpretation of reduced linear/unitary dynamics |
| `FROR_dual_layer_profile.md` | interpretive bridge between potential and fixed layers |
| `FROR_experiment_registry.md` | registry of profile-level and claim-level evidence obligations |
| `FROR_quantum_protocol_contour.md` | unified protocol contour across the whole stack |

------------------------------------------------------------------------

## 4. Matrix: assumptions, artifacts, tests, non-support

| component | core assumptions | required artifacts | support criteria | non-support criteria |
|---|---|---|---|---|
| Hilbert-like encoding | path classes can be aggregated; phase-like structure is definable; composition is meaningful | path-class spec; amplitude/phase assignment rule; composition test cases | amplitude composition explains observations better than count-only baselines on the chosen class | no stable phase structure or systematic failure of compositional amplitude aggregation |
| Born-like probability | amplitude aggregation is available; probability depends on class-level aggregate rather than raw path count alone | path-count baseline; amplitude baseline; normalization rule; comparative fit report | Born-like form is stable and outperforms pure count baselines without breaking composition | count baseline is sufficient or `|psi|^2` fails systematically when interference-like structure is claimed |
| measurement-like fixation | fixation operator `F` is explicit; pre/post-fixation layers are distinguishable; fixed outcomes leave stable traces | explicit `F`; outcome trace format; fixation-cost trace; rollback/unavailability trace | post-fixation description is measurably different from pre-fixation alternative bookkeeping and is consistent with resource loss | no reproducible difference between pre-fixation and post-fixation regimes or no coherent fixation criterion |
| Schrodinger-like reduced dynamics | coarse-grained classes admit reduced dynamics; norm-like quantity is preserved in the reversible regime; paid fixation can be separated | reduced linear model; norm-conservation checks; generator reconstruction; non-unitary comparison models | reduced linear or near-unitary form is stable in the reversible regime and degrades in the fixation regime as expected | linear/unitary reduction fails systematically or is not better than non-unitary alternatives in the same regime |

------------------------------------------------------------------------

## 5. Minimal reproducible artifact package

Any future execution pass on the quantum-like stack should produce at
least:

1. a path-class construction spec;
2. an amplitude aggregation rule or an explicit statement that no valid
   rule was found;
3. a baseline count-only model;
4. a reduced linear-dynamics candidate when Schrodinger-like testing is
   attempted;
5. norm-conservation checks for the no-fixation regime;
6. fixation / post-fixation traces showing the transition into an
   outcome-trace regime;
7. comparative reports against simpler baselines;
8. a non-support summary, not only a success narrative.

------------------------------------------------------------------------

## 6. Registry alignment

At minimum the contour must stay aligned with:

- `FROR-PROF-SCH-01` in [FROR_experiment_registry](./FROR_experiment_registry.md)

Candidate additional registry items, if the stack becomes more explicit:

- `FROR-PROF-HILB-01` --- Hilbert-like amplitude encoding
- `FROR-PROF-BORN-01` --- Born-like probability
- `FROR-PROF-MEAS-01` --- measurement-like fixation

These should remain profile-level registry items unless they later satisfy
the stricter claim workflow.

------------------------------------------------------------------------

## 7. Support and non-support discipline

The contour is only valid if each component has both:

- a positive support criterion;
- a concrete non-support criterion.

Forbidden failure mode:

- writing the profile as if any partial resemblance to quantum language
  already counts as evidence for the whole stack.

Correct discipline:

- support is component-local first;
- cross-component integration comes second;
- no component inherits support merely because an adjacent profile looked
  plausible.

------------------------------------------------------------------------

## 8. Boundary with Core

Nothing in this contour changes the canonical FROR core:

- no new axiom;
- no direct upgrade of Born/Hilbert/measurement/Schrodinger language into
  `Core`;
- no claim that FROR has derived quantum mechanics.

If a future pass wants to raise maturity, it must do so through explicit
registry items, artifacts, and the existing claim workflow.

------------------------------------------------------------------------

## 9. Recommended execution order

1. Hilbert-like encoding:
   define path classes and amplitude aggregation assumptions
2. Born-like probability:
   compare `|psi|^2` against count-only baselines
3. measurement-like fixation:
   define pre/post-fixation trace distinction
4. Schrodinger-like reduced dynamics:
   attempt reduced linear reconstruction only after the previous layers
   are operationally specified

This order prevents the stack from starting with the strongest claim
before the weaker prerequisites are operationalized.

------------------------------------------------------------------------

## 10. Short form

Quantum Protocol Contour exists to make the FROR quantum-like stack
auditable and executable without overstating what the corpus has already
proved.
