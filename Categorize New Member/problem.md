# Categorize New Member

The Western Suburbs Croquet Club has two membership categories: **Senior** and **Open**. Given each applicant’s age and handicap, return which category they belong in.

A member is **Senior** only if both are true:

- age ≥ **55**
- handicap > **7**

Otherwise they are **Open**.

Handicaps range from `-2` to `+26`. Lower handicap means a better player.

## Input / output

Each applicant is a pair `[age, handicap]`. Return a list of `"Senior"` or `"Open"` in the same order.

```text
open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]])
# → ["Open", "Open", "Senior", "Open", "Open", "Senior"]
```

| Age | Handicap | Category | Why                         |
|-----|----------|----------|-----------------------------|
| 18  | 20       | Open     | age < 55                    |
| 45  | 2        | Open     | age < 55                    |
| 61  | 12       | Senior   | age ≥ 55 and handicap > 7   |
| 37  | 6        | Open     | age < 55                    |
| 21  | 21       | Open     | age < 55                    |
| 78  | 9        | Senior   | age ≥ 55 and handicap > 7   |

## Insight

Walk the list once. For each pair, both conditions must hold:

```text
age >= 55  and  handicap > 7  →  "Senior"
otherwise                     →  "Open"
```

An age of 55 with handicap 7 is still **Open** — handicap must be **strictly greater** than 7.
