# Next Smaller Number with the Same Digits

Given a positive integer, return the **next smaller** positive integer that uses exactly the same digits.

If no such number exists, or if it would start with `0`, return `-1`. Tests include very large numbers — treat the value as digits, not by enumerating all permutations.

This is the inverse of *Next bigger number with the same digits*.

```text
next_smaller(21)    # → 12
next_smaller(531)   # → 513
next_smaller(2071)  # → 2017
next_smaller(9)     # → -1
next_smaller(135)   # → -1
next_smaller(1027)  # → -1   (0721 would have a leading zero)
```

## Example

`next_smaller(531)` — digits `[5, 3, 1]`

| Step | What | Result |
|------|------|--------|
| 1 | Rightmost place a drop is possible: `3 > 1` | pivot = `3` |
| 2 | To the right, largest digit still **smaller** than `3` | `1` |
| 3 | Swap | `[5, 1, 3]` |
| 4 | Sort the suffix after the pivot **descending** (largest leftover) | `[5, 1, 3]` → `513` |

`1027` follows the same steps to `0721`, which is invalid → `-1`.

## Insight

You want the largest number that is still smaller than `n`. Scan from the right for the first digit that is **greater** than its neighbor (a descent). That is the pivot — everything to its right is already the smallest arrangement of those digits.

```text
find rightmost i where digits[i] > digits[i+1]
swap digits[i] with the largest digit to the right that is still < digits[i]
sort digits[i+1:] descending
if digits[0] == '0'  →  -1
```

No descent means the digits are non-decreasing left to right (`135`, `9`) — already the smallest permutation → `-1`.
