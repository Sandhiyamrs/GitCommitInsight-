# Architecture Overview

GitCommitInsight follows a modular, rule-based architecture
to analyze Git commit history and generate insights.

---

## High-Level Flow

1. **CLI**
   - Entry point for the user.
   - Parses arguments and triggers analysis.

2. **Git Reader**
   - Reads commit history using Git commands.
   - Normalizes raw commit data.

3. **Analyzer**
   - Coordinates execution of all analysis checks.

4. **Checks**
   - Independent, pluggable rules.
   - Each check analyzes one aspect of commit behavior.

5. **Report Generator**
   - Aggregates results.
   - Outputs structured reports (JSON, Markdown).

---

## Module Responsibilities

| Module | Responsibility |
|------|----------------|
| `cli/` | User interaction |
| `core/` | Business logic |
| `checks/` | Analysis rules |
| `utils/` | Shared helpers |
| `output/` | Generated reports |

---

## Design Principles

- Single Responsibility
- Loose Coupling
- Easy Extensibility
- Testability

---

## Adding a New Check

1. Create a new file in `checks/`
2. Implement `analyze_*()` function
3. Register it in `analyzer.py`
4. Add unit tests

---

## Future Improvements

- Plugin system
- Visualization layer
- Configurable rule sets
