# Delete Occurrences of an Element if it Occurs More Than N Times

Given a list and a number `n`, build a new list that keeps each value **at most `n` times**, in the original order. Extra copies beyond `n` are dropped.

```text
delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 2)  # → [1, 2, 3, 1, 2, 3]
delete_nth([20, 37, 20, 21], 1)          # → [20, 37, 21]
```

## Example

`delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 2)` — keep each number at most twice.

| Value | Seen so far | Keep? | Result so far        |
|-------|-------------|-------|----------------------|
| 1     | 0           | yes   | `[1]`                |
| 2     | 0           | yes   | `[1, 2]`             |
| 3     | 0           | yes   | `[1, 2, 3]`          |
| 1     | 1           | yes   | `[1, 2, 3, 1]`       |
| 2     | 1           | yes   | `[1, 2, 3, 1, 2]`    |
| 1     | 2           | no    | `[1, 2, 3, 1, 2]`    |
| 2     | 2           | no    | `[1, 2, 3, 1, 2]`    |
| 3     | 1           | yes   | `[1, 2, 3, 1, 2, 3]` |

The third `1` and third `2` are dropped. The second `3` is kept.

## Insight

Walk the list once. Count how many times each value has already been kept. Append only while that count is still below `n`:

```text
count[x] < n  →  keep x, increment count[x]
otherwise     →  skip
```

Order never changes — later copies are the ones that get cut.
