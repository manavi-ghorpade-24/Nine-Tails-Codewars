# Dots on Domino's Bones

A double-`n` set of dominoes contains every unordered pair of values from `0` to `n`. Tiles like `2 | 5` and `5 | 2` are the same, and doubles like `1 | 1` are included.

Each pip (dot) is a diamond. Given `n` — the maximum number of pips on one half of a tile — return the **total number of pips** on the whole set.

Constraints: `0 < n < 1000`

## Example

For `n = 2` the tiles are:

```text
0 | 0    0 | 1    0 | 2
         1 | 1    1 | 2
                  2 | 2
```

Sum of all pips: `0 + 1 + 2 + 1 + 1 + 1 + 2 + 2 + 2 = 12`

```text
dots_on_domino_bones(2)   # → 12
dots_on_domino_bones(3)   # → 30
dots_on_domino_bones(20)  # → 4620
```

| `n` | Result |
|-----|--------|
| 2   | 12     |
| 3   | 30     |
| 20  | 4620   |

## Insight

Every tile is a pair `(i, j)` with `0 ≤ i ≤ j ≤ n`. Nested loops over that range, adding `i + j`, give the total.

Each value `k` from `0` to `n` appears **`n + 2` times** across the set (both halves of a double count). The sum of `0 … n` is `n(n + 1) / 2`, so:

```text
total = n(n + 1)(n + 2) / 2
```
