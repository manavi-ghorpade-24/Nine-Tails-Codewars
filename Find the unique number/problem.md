# Find the Unique Number

There is an array of numbers. All values are equal except **one**. Return that unique number.

The array has at least 3 elements. Tests include very large arrays, so avoid an `O(n²)` approach.

```text
find_uniq([1, 1, 1, 2, 1, 1])     # → 2
find_uniq([0, 0, 0.55, 0, 0])     # → 0.55
```

## Example

`find_uniq([1, 1, 1, 2, 1, 1])`

| Index | Value | Unique? |
|-------|-------|---------|
| 0     | 1     | no      |
| 1     | 1     | no      |
| 2     | 1     | no      |
| 3     | 2     | **yes** |
| 4     | 1     | no      |
| 5     | 1     | no      |

## Insight

Compare the first three elements to learn the **common** number, then scan once for the value that differs:

```text
arr[0] == arr[1]  →  common is arr[0]
arr[1] == arr[2]  →  common is arr[1]   (unique is first)
otherwise         →  common is arr[0]   (unique is arr[1])
```

Then return the first `num != common`. One pass after a constant-time check is enough for the large test arrays.
