---
title: "Профиль домена: Human Multicontext Override"
date: 2026-03-01
tags: [CDM, Context, CtxL, domain, human, multicontext]
citekey: cdm_context_domain_human_multicontext_profile_ru_2026
---

# Профиль домена: Human Multicontext Override

## 1. Назначение

Документ задает минимальный доменный override для системы `Y=Human`
поверх:
- `Context-Multicontext-Applicability-Profile.md` (default),
- `Context-Coordination-Protocol.md` (CBP).

Цель: воспроизводимо учитывать межконтекстные влияния между
`C_bio`, `C_cog`, `C_soc` при оценке `Defined/Applicable/Result`.

---

## 2. Контекстная модель домена Human

Базовые контексты:

1. `C_bio`:
- физиология, сон, нейроэндокринные маркеры, соматические ограничения.

2. `C_cog`:
- когнитивные интерпретации, тревожность, внимание, стратегии принятия решений.

3. `C_soc`:
- социальные роли, давление среды, нормы, институциональные ограничения.

Принцип:
- все три контекста относятся к одной системе `Human`;
- конфликты между ними трактуются как межконтекстные, а не как межсистемные.

---

## 3. Минимальный YAML override

```yaml
multicontext_applicability_profile:
  system_id: "Human"
  thresholds:
    impact_strength_theta: 0.40
    translate_conf_tau: 0.70
  impact_matrix:
    - from: C_cog
      to: C_bio
      strength: 0.80
      lag: "P1D"
      condition: "anxiety_index > 0.60"
      confidence: 0.85
    - from: C_soc
      to: C_cog
      strength: 0.75
      lag: "PT6H"
      condition: "role_pressure_index > 0.55"
      confidence: 0.80
    - from: C_bio
      to: C_cog
      strength: 0.70
      lag: "PT12H"
      condition: "sleep_deficit_hours >= 2"
      confidence: 0.82
    - from: C_soc
      to: C_bio
      strength: 0.50
      lag: "P2D"
      condition: "chronic_stress_score > 0.50"
      confidence: 0.72
  priorities:
    - C_bio
    - C_cog
    - C_soc
  result_zero_contract:
    require_zero_class: true
    require_source_context: true
    require_affected_contexts: true
    require_reason_trace_ref: true
  escalation:
    force_cbp_on_conflict: true
```

---

## 4. Интерпретация Result=0 для Human

Для домена Human рекомендуется:

1. `AF_sem`:
- Intent логически/семантически не принадлежит активному контексту.

2. `AF_epi`:
- недостаточно наблюдений/данных для контекста (например, нет валидных маркеров).

3. `AF_sto`:
- стохастическая нестабильность не позволяет принять безопасное решение.

4. `mixed`:
- одновременно срабатывают несколько причин (например, `AF_epi + AF_sto`).

---

## 5. Re-evaluation правила

После обновления одного контекста:

1. вычислить `ReevalSet` по `impact_strength_theta`;
2. пересчитать `Defined/Applicable` для всех контекстов из `ReevalSet`;
3. при конфликте приоритетов или низком `confidence` запускать CBP.

Практический минимум:

- изменение `C_cog` с высокой тревожностью всегда триггерит переоценку `C_bio`;
- значимое изменение `C_soc` (роль/давление) триггерит переоценку `C_cog`;
- дефицит сна в `C_bio` триггерит переоценку `C_cog`.

---

## 6. Минимальные тесты воспроизводимости

1. `T1`:
- рост `anxiety_index` в `C_cog` должен менять applicability минимум в одном из
  сценариев `C_bio`.

2. `T2`:
- рост `role_pressure_index` в `C_soc` должен менять applicability в `C_cog`.

3. `T3`:
- при одинаковом входе и policy выход CBP (`Aligned/Forked/Blocked`) повторяем.

4. `T4`:
- при `Result=0` всегда заполнены `zero_class`, `source_context`,
  `affected_contexts`, `reason_trace_ref`.

---

## 7. Статус

Профиль рекомендован как базовый human-override и может уточняться
клиническим/организационным доменным под-профилем.
