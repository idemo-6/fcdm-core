---
title: "Профиль: Operator Novelty Constraint (governance-level)"
date: 2026-03-01
tags: [CDM, Operators, profile, governance, novelty]
citekey: cdm_operator_novelty_constraint_profile_ru_2026
---

# Профиль: Operator Novelty Constraint (governance-level)

## 1. Назначение

Профиль задает проверяемое governance-ограничение на «новизну операторов» без метафизических предпосылок.

---

## 2. Нормативная граница

Это профиль, не канон.

Статус:
- optional worldview/governance profile;
- не обязателен для базового CDM conformance.

Опорные документы:
- `ChangeOperators (каноническая)`
- `Governance: Canon <-> DSL Synchronization`
- `Context-Coordination-Policy-*` (доменные)

---

## 3. Операционная формулировка

Пусть задан доменный реестр операторов `OperatorUniverse_vN`.

Ограничение:
1. Исполнение допускает только операторы из `OperatorUniverse_vN`.
2. Любой кандидат вне реестра маркируется как `operator_novelty_candidate`.
3. Использование кандидата в `prod` запрещено до процедуры расширения реестра.

---

## 4. Процедура расширения реестра

Для `operator_novelty_candidate` требуется:
1. формальная спецификация и границы применимости;
2. анализ совместимости с текущим каноном/профилями;
3. risk/safety review;
4. approval governance-процессом;
5. выпуск новой версии `OperatorUniverse_v(N+1)`.

До завершения процедуры кандидат допускается только в `dev/sandbox` с явной маркировкой.

---

## 5. Инварианты профиля

1. `I_nov_1` — Версионность  
   Любой запуск фиксирует `operator_universe_version`.

2. `I_nov_2` — Явность новизны  
   Неизвестные операторы не «молча» исполняются.

3. `I_nov_3` — Прод-контроль  
   `prod` использует только утвержденный реестр.

---

## 6. Trace в evaluate

Минимально фиксировать:
1. `operator_universe_version`
2. `unknown_ops_detected` (bool)
3. `unknown_ops_list`
4. `novelty_decision` (`blocked|sandbox_only|approved`)

---

## 7. Сопоставление с legacy "no-new-operators"

Legacy-тезис «новых операторов не существует» в CDM заменяется на проверяемую инженерную норму:
- «новые для реестра операторы не входят в production до процедуры утверждения».

---

## 8. Заключение

Профиль снимает метафизическую жесткость legacy-ограничения и сохраняет строгий контроль новизны операторов в инженерно проверяемой форме.

