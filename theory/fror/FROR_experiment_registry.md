# FROR: Реестр экспериментов и доказательных обязательств

(единый рабочий реестр для того, что в FROR требует формального подтверждения или эмпирической проверки)

## Связанные заметки
- [FROR_architecture_v2](./FROR_architecture_v2.md)
- [FROR_axioms_v0_2](./FROR_axioms_v0_2.md)
- [FROR_normalizations_invariants](./FROR_normalizations_invariants.md)
- [FROR_class_measurement](./FROR_class_measurement.md)
- [claims_registry](./claims_registry.yaml)
- [claim_event_log](./claim_event_log.yaml)

---

## 0. Назначение

Документ фиксирует:
1. какие утверждения FROR считаются доказательными обязательствами;
2. какой тип верификации нужен (формальная/экспериментальная);
3. какие протоколы, метрики и критерии считаются достаточными;
4. что считается неподтверждением/опровержением.

---

## 1. Шаблон записи (обязательные поля)

Для каждого пункта реестра должны быть заданы:
- `item_id`
- `statement`
- `current_status`
- `verification_type`: `Formal` | `Empirical` | `Mixed`
- `primary_protocol`
- `required_artifacts`
- `support_criteria`
- `non_support_criteria`
- `priority`

---

## 2. Реестр по claims (claims_registry.yaml)

| item_id | statement | current_status | verification_type | primary_protocol | required_artifacts | support_criteria | non_support_criteria | priority |
|---|---|---|---|---|---|---|---|---|
| FROR-CLM-001 | Tri-class representation threshold (`K(R)>=3`) | Core | Formal | `FROR_axioms_v0_2.md` (A3, T2) + finite-model sanity | proof note + finite counterexample scan report | отсутствие логических контрпримеров в формализации A1..A5; `K(R)<3` не реализует 3-классовую стратегию | найдена модель с `K(R)<3`, устойчиво реализующая 3-классовое внутреннее различение | P1 |
| FROR-CLM-002 | Effective irreversibility from distinguishability deficit | Core | Mixed | `FROR_axioms_v0_2.md` (A5, D8, T1) + rollback-cost benchmark | simulation logs (`N_t`, `K(R_t)`, `DeltaI_miss`, `C_rb`) + reproducible scripts | при `DeltaI_miss>0` минимальная цена rollback монотонно растет в пределах статистической устойчивости | воспроизводимый режим rollback без доп. цены при устойчивом `DeltaI_miss>0` | P1 |
| FROR-CLM-003 | `tau` и `D` различимы как счетчики | Core | Empirical | controlled traces with `c_fix`/`c_bg` decomposition | trace dataset с шагами (`c_fix`,`c_bg`,`tau`,`D`) | есть серии с `c_bg>0` и `c_fix=0`, где `D` растет при неизменном `tau` | невозможность построить согласованный режим раздельного учета `c_fix` и `c_bg` | P1 |
| FROR-CLM-004 | C1..C5 как anti-hack constraints | Protocol | Empirical | adversarial normalization suite (pass/fail under C1..C5) | benchmark matrix + attack cases + negative controls | при соблюдении C1..C5 исчезают устойчивые «подгонки» на независимых сериях | сохраняется воспроизводимая подгонка при формальном выполнении C1..C5 | P1 |
| FROR-CLM-005 | Memory threshold `M_O>=2` for tri-class asymmetry | Protocol | Empirical | `FROR_distinguishability_resource_threshold.md` protocol | CSV runs by `M_O`, test report, significance corrections | при `M_O=1` нет устойчивой трихотомии без внешнего ресурса; при `M_O>=2` эффект воспроизводим | устойчивое трихотомное различение при `M_O=1` без внешнего оракула/памяти | P1 |
| FROR-CLM-006 | `d_s(G0)≈3` as stable phase/attractor | Conjecture | Empirical | preregistered protocol: `FROR_class_measurement.md` + `FROR_ds3_attractor.md` | prereg file, power/sensitivity plan, multiple-testing correction, finite-size report, negative results | устойчивый режим/плато около `d_s≈3` после статистических поправок и finite-size scaling на независимых классах графов | плато не воспроизводится или систематически сильнее вне окрестности `d_s≈3` | P1 |
| FROR-CLM-007 | SLOT stability peak near `d_s≈3` | Conjecture | Empirical | preregistered SLOT scans over graph families | `Psi(ds)` curves + threshold robustness report + negative runs | максимум устойчивости SLOT воспроизводим вблизи `d_s≈3` при контролях | максимум систематически смещен/исчезает при корректных контролях | P1 |
| FROR-CLM-008 | Cross-domain portability of FROR invariants | Protocol | Mixed | DomainLexicon V1..V4 + cross-domain replication set | mapping specs per domain + invariant checks + failure logs | инварианты I1..I6 сохраняются при валидных отображениях в нескольких доменах | конфликт инвариантов при корректном `Core -> Terms_D` отображении | P2 |
| FROR-CLM-009 | Delayed-commit policy reduces long-horizon `E[tau_long]` under finite budget | Conjecture | Empirical | toy-MDP with irreversible commits (`FROR_agency_profile.md`, E1) | environment spec + policy baselines (reactive/forecast/delayed) + run logs + stats report | delayed-commit устойчиво снижает `E[tau_long]` при сопоставимых ограничениях | reactive baseline систематически лучше delayed-commit в устойчивых сериях | P2 |
| FROR-CLM-010 | Increasing `gamma` raises share of strategies minimizing `E[tau_long_sys]` | Conjecture | Empirical | repeated multi-agent dilemma (`FROR_agency_profile.md`, E2) | game config + sweep over `gamma` + cooperation/`tau_sys` traces + robustness checks | при росте `gamma` растет доля стратегий с меньшим `tau_sys` и выше устойчивость кооперации | отсутствие тренда или обратный тренд после контролей | P2 |
| FROR-CLM-011 | Money metrics are a noisy proxy for `tau_social` | Conjecture | Mixed | ABM with externalities + socio-economic mapping (`FROR_agency_profile.md`, E3) | operational `tau_social` metric + money indicators + externality regimes + error analysis | в низко-внешнеэффектном режиме прокси-корреляция есть, при high-externality ошибку можно воспроизвести | нет устойчивой связи money-метрик с `tau_social` даже в контролируемых режимах | P2 |
| FROR-CLM-012 | Observer-level entropy arrow from finite distinguishability | Conjecture | Mixed | reversible microdynamics + observer coarse-graining stress-test (`N_t`,`K(R_t)`) | reversible simulator spec + observer map `F` + `S_defect/tau` traces + control runs | при устойчивом `N_t>K(R_t)` наблюдается направленный рост наблюдаемого дефекта/стрелки на уровне наблюдателя | есть устойчивые режимы с `N_t>K(R_t)` без наблюдаемой стрелки при корректных контролях | P2 |
| FROR-CLM-013 | Low-externality regime for money-to-`tau_social` approximation | Conjecture | Mixed | ABM regime sweep over externalities and information asymmetry | calibrated `tau_social` + money metrics + regime grid + approximation error report | существует область параметров с устойчиво малой систематической ошибкой money->`tau_social` | высокая систематическая ошибка сохраняется во всей low-distortion области | P2 |
| FROR-CLM-014 | Norm persistence tracks long-horizon `tau_sys` minimization | Conjecture | Empirical | repeated-game norm evolution with persistence tracking | norm-dynamics logs + persistence metrics + `E[tau_long_sys]` comparisons | долгоживущие нормы статистически ассоциированы с меньшим `E[tau_long_sys]` относительно жадных baseline | устойчиво сохраняющиеся нормы не дают выигрыша по `E[tau_long_sys]` | P2 |
| FROR-CLM-015 | Internal `tau` accounting reduces long-horizon catastrophic errors | Conjecture | Empirical | matched-agent benchmark (with/without internal `tau` accounting) | benchmark suite + catastrophic-error definition + OOD long-horizon traces + stats | модели с внутренним `tau`-учетом снижают частоту катастрофических ошибок в сопоставимых условиях | отсутствие выигрыша или ухудшение при устойчивых повторениях | P2 |
| FROR-CLM-016 | Cross-domain calibration via invariant dimensionless groups | Conjecture | Mixed | multi-domain calibration study (physics/computing/cognitive/social mappings) | explicit invariant groups + mapping specs + cross-domain prediction tests | перенос предсказаний сохраняется после калибровки без нарушения I1..I6 | переносимая калибровка не удается без конфликтов инвариантов | P3 |
| FROR-CLM-017 | Typical rollback cost is exponential in `DeltaI_miss` | Conjecture | Empirical | branching-process rollback complexity benchmark | process-family definitions + optimal rollback solver + scaling report vs `DeltaI_miss` | в широком классе ветвящихся процессов нижняя граница rollback-cost согласуется с экспоненциальным ростом | устойчиво подтверждается субэкспоненциальный scaling на широком классе | P2 |

---

## 3. Реестр по профильным гипотезам (вне claims_registry)

| item_id | statement | layer_status | verification_type | primary_protocol | required_artifacts | support_criteria | non_support_criteria | priority |
|---|---|---|---|---|---|---|---|---|
| FROR-PROF-REL-01 | Relativity-like effective symmetry regime | Conjectural profile | Empirical | `FROR_relativity_profile.md` tests | frame-change invariance report + continuum stability checks | корреляционные статистики инвариантны в заявленном эффективном классе | устойчивое нарушение заявленной инвариантности | P2 |
| FROR-PROF-LS-01 | Finite `c_eff` correlation-speed bound | Conjectural profile | Empirical | `FROR_light_speed_profile.md` program | front-propagation dataset in `(r,tau)` + robustness report | конечный устойчивый `c_eff` на одном классе моделей | отсутствие устойчивого конечного `c_eff` | P2 |
| FROR-PROF-GR-01 | GR-like effective geometry | Conjectural profile | Empirical | `FROR_gravity_profile.md` program | geodesic-fit benchmarks + curvature-path correlation | geodesic-like модели стабильно лучше базовых альтернатив | нет устойчивого выигрыша geodesic-like модели | P3 |
| FROR-PROF-SCH-01 | Schrodinger-like reduced dynamics | Conjectural-to-Protocol | Mixed | `FROR_schrodinger_profile.md` program | reduced linear model + norm-conservation checks | в обратимом режиме устойчиво восстанавливается линейная/почти унитарная форма | линейная модель систематически хуже неунитарных альтернатив | P2 |
| FROR-PROF-SM-01 | SM/QFT mappings from FROR profiles | Conjectural profile | Empirical | `FROR_sm_profile.md` + `FROR_electro_profile.md` | mapping assumptions + comparative fit reports | есть ограниченный воспроизводимый класс явлений, где профильная карта работает лучше baseline | отсутствие устойчивых улучшений или сильная нестабильность при малых вариациях | P3 |

---

## 4. Минимальный пакет артефактов для claim-уровня

Для каждого пункта с `verification_type=Empirical` или `Mixed`:
1. preregistered-спецификация (гипотеза, primary endpoint, критерии неподтверждения);
2. репродуцируемый скрипт/конфиг запуска;
3. сырые результаты + агрегированные метрики;
4. отчет по статистике:
   - sensitivity/power,
   - multiple testing correction,
   - finite-size scaling;
5. отчет отрицательных результатов;
6. краткий verdict: `Supported` / `Not Supported` / `Inconclusive`.

---

## 5. Порядок выполнения (рекомендуемые волны)

Волна 1 (критические для канона): `CLM-002`, `CLM-003`, `CLM-004`, `CLM-005`.

Волна 2 (центральные гипотезы структуры): `CLM-006`, `CLM-007`.

Волна 3 (переносимость и агентный слой): `CLM-008`, `CLM-009`, `CLM-010`, `CLM-011`, `CLM-012`, `CLM-013`, `CLM-014`, `CLM-015`, `CLM-017`.

Волна 4 (междоменная калибровка и профильные режимы): `CLM-016`, `FROR-PROF-*`.

---

## 6. Операционное правило обновления

После каждой завершенной серии:
1. обновить этот реестр (статус и ссылки на артефакты);
2. внести событие в `claim_event_log.yaml` при изменении зрелости claim;
3. при необходимости обновить `claims_registry.yaml`;
4. запустить:
`python3 fcdm-core/theory/fror/check_claim_status_transitions.py --registry fcdm-core/theory/fror/claims_registry.yaml --events fcdm-core/theory/fror/claim_event_log.yaml`.
