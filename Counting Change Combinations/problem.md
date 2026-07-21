# Counting Change Combinations

Count how many **different combinations** of coins add up to `money`. Order does not matter (`1+1+2` is the same as `2+1+1`). You have an unlimited supply of each denomination.

If no combination works, return `0`. The denominations in `coins` are unique.

```text
count_change(4, [1, 2])     # → 3
count_change(10, [5, 2, 3]) # → 4
count_change(11, [5, 7])    # → 0
```

## Example

`count_change(4, [1, 2])`

| Combination   | Counts as |
|---------------|-----------|
| `1+1+1+1`     | 1 way     |
| `1+1+2`       | 1 way     |
| `2+2`         | 1 way     |
| `2+1+1`       | same as `1+1+2` |

Total: **3**

`count_change(10, [5, 2, 3])` → `5+5`, `5+3+2`, `3+3+2+2`, `2+2+2+2+2` → **4**

## Insight

Walk the coin list from left to right so each combination is built in one order only. At coin `i`, either take another of that coin (stay on `i`) or skip it (move to `i+1`):

```text
target == 0          →  one valid combination
target < 0           →  dead end
coins[i] fits        →  pick it again (same index)
always               →  skip to the next denomination
```

That is unbounded-knapsack backtracking. `money == 0` is one way (use no coins). An empty `coins` list with `money > 0` is zero ways.
