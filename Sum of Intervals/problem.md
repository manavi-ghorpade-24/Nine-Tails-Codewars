# Sum of Intervals

Given a list of intervals, return the **total length** of their union. Overlapping (or nested) intervals count only once.

An interval is a pair `[start, end]` with `start < end`. Its length is `end - start` (so `[1, 5]` has length `4`).

All tested intervals lie in `[-1_000_000_000, 1_000_000_000]`. A naive “mark every integer” approach will time out.

```text
sum_of_intervals([[1, 2], [6, 10], [11, 15]])                 # → 9
sum_of_intervals([[1, 4], [7, 10], [3, 5]])                   # → 7
sum_of_intervals([[1, 5], [10, 20], [1, 6], [16, 19], [5, 11]])  # → 19
sum_of_intervals([[0, 20], [-100000000, 10], [30, 40]])       # → 100000030
```

## Example

`[[1, 4], [7, 10], [3, 5]]`

`[1, 4]` and `[3, 5]` overlap, so they merge to `[1, 5]` (length `4`). `[7, 10]` stays (length `3`).

```text
1  2  3  4  5        7  8  9  10
|-----------|        |----------|
      |-----|
```

Total: `4 + 3 = 7`

## Insight

Sort intervals by start, then sweep once, merging into a current `[first, last]`:

```text
next.start < last  →  still overlapping: last = max(last, next.end)
otherwise          →  close the current interval, start a new one
```

Add `last - first` each time an interval is closed (including the last one). Sorting plus a linear merge is enough for the large-range tests.
