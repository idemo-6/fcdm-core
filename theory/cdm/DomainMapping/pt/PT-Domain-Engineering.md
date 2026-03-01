---
title: "Доменный пример: PhaseTransition в инженерных системах"
date: 2026-02-26
tags: [CDM, PhaseTransition, engineering, example]
---

# PhaseTransition в инженерных системах

Связанные канонические документы:
- Спецификация PhaseTransition
- [[DomainLexicon]]

## Интерпретация

PhaseTransition соответствует:

- деградации системы
- отказу
- переключению режима
- восстановлению

## Order Parameter

Примеры:

- нагрузка
- температура
- частота ошибок
- задержка

## Пример

Система → отказ:

Start: нормальная работа  
In‑Transition: рост ошибок  
End: отказ  

result = true → отказ произошёл
