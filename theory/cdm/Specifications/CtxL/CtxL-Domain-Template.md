---
title: "Шаблон: Domain CtxL Specification"
date: 2026-02-28
tags: [CDM, CtxL, domain, template]
---

# Шаблон: Domain CtxL Specification

## 1. Domain

- Domain ID:
- Domain Name:
- Связанный DomainLexicon:

---

## 2. Контексты домена

- `C_avail(Y)`:
- `C_candidates(Y, t)`:
- правило выбора `C_active^k(t)` для ветки `k`:
- условия появления межконтекстной дивергенции:

---

## 3. Семантические пространства

Для каждого ключевого контекста:
- `SemanticSpace(Ci)`:
- примеры `P in SemanticSpace(Ci)`:
- примеры `P notin SemanticSpace(Ci)`:

---

## 4. Applicable(Intent, C_active, LC_phase)

Определить:
- критерии `Applicable=true`;
- критерии `ApplicabilityFailure`;
- маппинг причин `AF_sem/AF_epi/AF_sto`.

---

## 5. Оценка Experience=0

Определить:
- как фиксируется `Result=0`;
- как выполняется `Classify0`;
- как результат `Classify0` влияет на следующий `ChangeFlow`.

---

## 6. Координационный контекст

Если используется `C_coord`, указать:
- источник координационных правил;
- приоритеты;
- правила трансляции между контекстами.

---

## 7. Тесты валидации

- T1: воспроизводимость `Truth(P, C)` в одном контексте;
- T2: корректное разделение дивергенции и противоречия;
- T3: корректная фиксация `Result=0 <=> ApplicabilityFailure`;
- T4: корректная классификация `AF_sem/AF_epi/AF_sto`.
