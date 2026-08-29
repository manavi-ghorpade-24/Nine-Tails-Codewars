# Smallest Possible Sum

Given an array `X` of positive integers, transform its elements by repeating this operation as many times as needed:

> If `X[i] > X[j]`, then `X[i] = X[i] - X[j]`

When no more transformations are possible, return the **sum** of the array (the smallest possible sum).

## Example

```text
solution([6, 9, 21])  # → 9
```

Successive transformations of `[6, 9, 21]`:

| Step | Array        | Operation              |
|------|--------------|------------------------|
| 1    | `[6, 9, 12]` | `X[2] = 21 - 9`        |
| 2    | `[6, 9, 6]`  | `X[2] = 12 - 6`        |
| 3    | `[6, 3, 6]`  | `X[1] = 9 - 6`         |
| 4    | `[6, 3, 3]`  | `X[2] = 6 - 3`         |
| 5    | `[3, 3, 3]`  | `X[0] = 6 - 3`         |

Final sum: **9**

## Performance

Tests include very large numbers and arrays of size **at least 30,000**. Write an efficient algorithm to avoid timeouts.

## Insight

The operation `X[i] -= X[j]` is Euclidean subtraction. Repeating it until all values are equal leaves every element as `gcd(X)`. The smallest possible sum is therefore:

```text
gcd(X) × len(X)
```
