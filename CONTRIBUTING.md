# Contributing to fcdm-core

## Principles

- This repository is the canonical theoretical core.
- Contributions must preserve domain-agnostic formulation.
- Domain implementation details must be submitted to downstream repositories.

## Workflow

- Use fork -> pull request.
- Keep commits attributable to authorship.
- Keep bridge changes explicit and testable via mapping/falsifiability criteria.

## Local hooks (recommended)

For FROR claim-status integrity checks, install repository hooks once:

```bash
bash scripts/install-git-hooks.sh
```

This enables:
- `pre-commit`: claim transition validation;
- `commit-msg`: requires `claim: FROR-CLM-XXX` when claim registry/event log changed;
- `pre-push`: transition validation before push.

## Licensing

By contributing, you agree your contribution is licensed under CC BY 4.0.
