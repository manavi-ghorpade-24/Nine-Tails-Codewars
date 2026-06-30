# Write Number in Expanded Form

Given a whole number greater than `0`, return it as a string in expanded form: each non-zero digit times its place value, joined with ` + `.

Zeros in the middle are skipped — they do not appear in the result.

```text
expanded_form(12)     # → "10 + 2"
expanded_form(45)     # → "40 + 5"
expanded_form(70304)  # → "70000 + 300 + 4"
```

## Example

`expanded_form(70304)`

| Digit | Place   | Term    | Keep? |
|-------|---------|---------|-------|
| 7     | 10000   | `70000` | yes   |
| 0     | 1000    | `0`     | no    |
| 3     | 100     | `300`   | yes   |
| 0     | 10      | `0`     | no    |
| 4     | 1       | `4`     | yes   |

Join with ` + `: `70000 + 300 + 4`

## Insight

Peel digits from the right. Multiply each by its place (`1`, `10`, `100`, …). Skip zeros, then reverse so the largest place comes first:

```text
digit * place  ≠  0  →  keep as a term
otherwise            →  skip
```

Join the terms with `" + "`.
