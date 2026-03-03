---
title: "CDM Profile: Claim Maturity (Conjecture/Protocol/Validated/Core)"
date: 2026-03-03
tags: [CDM, claim-maturity, profile, governance, FROR]
citekey: cdm_claim_maturity_profile_ru_2026
---

# CDM Profile: Claim Maturity

## 1. Назначение

Документ задает профиль применения статусов зрелости утверждений в CDM/FROR:

- `Conjecture`
- `Protocol`
- `Validated`
- `Core`

Профиль совместим с state-derived versioning и отделяет:
- состояние сущности (`EntityVersion`),
- зрелость тезиса (`ClaimStatus`).

---

## 2. Нормативная база

- [[fcdm-core/theory/cdm/Specifications/Versioning/Versioning-Canonical|Versioning-Canonical]]
- [[fcdm-core/theory/cdm/Specifications/Versioning/Version-Derivation-Policy|Version-Derivation-Policy]]
- [[fcdm-core/theory/fror/FROR_architecture_v2|FROR Architecture V2]]
- [MMCF Claim Maturity Canonical](../../../../mmcf-docs/methodology/Claim-Maturity-Canonical.md)

---

## 3. Базовые правила профиля

1. `ClaimStatus` хранится на уровне утверждения (`ClaimId`), а не документа.
2. `ClaimStatus` не кодируется в `v.<inc>.<lc>.<cf>.<cfp>`.
3. Изменение статуса утверждения должно иметь трассу событий и evidence.
4. Переходы статусов последовательные: `Conjecture -> Protocol -> Validated -> Core`.
5. Skip-level переходы запрещены (кроме audit override).

---

## 4. Минимальный атрибутный контракт claim

Для каждого утверждения рекомендуется фиксировать:

- `claim_id`
- `statement`
- `scope`
- `assumptions`
- `falsification`
- `status`
- `evidence_refs`
- `updated_at`

---

## 5. Gate-критерии переходов

### 5.1 `Conjecture -> Protocol`

Необходимо:
- воспроизводимый протокол проверки;
- метрики;
- критерии прохождения/провала;
- анти-примеры.

### 5.2 `Protocol -> Validated`

Необходимо:
- результат(ы) по протоколу;
- evidence-артефакты;
- прохождение контрольных режимов.

### 5.3 `Validated -> Core`

Необходимо:
- проверка на конфликт с действующим каноном;
- согласование с инвариантами и критериями соответствующего слоя;
- фиксация канонического источника истины.

---

## 6. Интеграция с FROR (профиль применения)

В FROR рекомендуется:
- маркировать ключевые тезисы `ClaimId`;
- отражать статус в таблице документа;
- хранить доказательные детали в профильном реестре (`claims_registry`).

Это позволяет разделить:
- архитектурную зрелость документа,
- зрелость конкретных утверждений.

---

## 7. Аудит и override

Override статуса допускается только в аварийном режиме с обязательными полями:
- `override_reason`
- `approved_by`
- `approved_at`
- `revalidation_plan`

После override обязателен возврат к state-derived статусу по событиям.
