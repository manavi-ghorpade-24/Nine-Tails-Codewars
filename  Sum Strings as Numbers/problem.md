# Sum Strings as Numbers

Given two integers as strings, return their **sum as a string**.

The strings contain only the digits `0`–`9`. Inputs can be huge (~a million digits), so do not convert the whole string with `int()` — add digit by digit.

```text
sum_strings("1", "2")      # → "3"
sum_strings("999", "1")    # → "1000"
sum_strings("001", "2")    # → "3"
sum_strings("0", "0")      # → "0"
```

## Example

`sum_strings("999", "1")` — add from the right, keep a carry:

| Step | Digit A | Digit B | Carry in | Sum | Write | Carry out |
|------|---------|---------|----------|-----|-------|-----------|
| 1    | 9       | 1       | 0        | 10  | `0`   | 1         |
| 2    | 9       | 0       | 1        | 10  | `0`   | 1         |
| 3    | 9       | 0       | 1        | 10  | `0`   | 1         |
| 4    | —       | —       | 1        | 1   | `1`   | 0         |

Digits were collected right-to-left (`0`, `0`, `0`, `1`), then reversed: `"1000"`.

## Insight

Schoolbook addition: walk both strings from the last character. Missing digits count as `0`. Continue while either string has digits left **or** a carry remains.

```text
total = a + b + carry
write  total % 10
carry  total // 10
```

Reverse the written digits, strip leading zeros, and return `"0"` if nothing is left (the sum was zero).
