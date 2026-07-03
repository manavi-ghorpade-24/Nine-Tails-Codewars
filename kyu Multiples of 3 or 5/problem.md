# Multiples of 3 or 5

Return the sum of all natural numbers **below** `n` that are multiples of `3` or `5`.

If `n` is negative or `0`, return `0`. A number that is a multiple of both `3` and `5` (i.e. of `15`) is counted **once**.

```text
solution(10)  # → 23   (3 + 5 + 6 + 9)
solution(0)   # → 0
```

## Example

`solution(10)` — numbers **below 10**:

| Number | Multiple of 3 or 5? |
|--------|---------------------|
| 1      | no                  |
| 2      | no                  |
| 3      | yes                 |
| 4      | no                  |
| 5      | yes                 |
| 6      | yes                 |
| 7      | no                  |
| 8      | no                  |
| 9      | yes                 |

Sum: `3 + 5 + 6 + 9 = 23`

## Insight

Looping to `n` works for small inputs, but the closed form is `O(1)`.

**Inclusion–exclusion.** Adding every multiple of 3 and every multiple of 5 counts multiples of 15 twice (`15`, `30`, …). Subtract them once:

```text
sum(3 or 5) = sum(multiples of 3) + sum(multiples of 5) − sum(multiples of 15)
```

**Arithmetic series.** Multiples of `k` below `n` are `k, 2k, …, m·k` where

```text
m = (n − 1) // k
```

Their sum is `k × (1 + 2 + … + m)`:

```text
k × m × (m + 1) / 2
```

So `solution(n)` is that formula for `k = 3`, plus `k = 5`, minus `k = 15`.
