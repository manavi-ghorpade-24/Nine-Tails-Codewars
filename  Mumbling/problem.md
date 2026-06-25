# Mumbling

Given a string of letters (`a–z` and `A–Z`), return a new string where the character at index `i` is repeated `i + 1` times, capitalized, and joined with `-`.

```text
accum("abcd")     # → "A-Bb-Ccc-Dddd"
accum("RqaEzty")  # → "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")     # → "C-Ww-Aaa-Tttt"
```

## Example

`accum("abcd")`

| Index | Letter | Repeat | Capitalized |
|-------|--------|--------|-------------|
| 0     | `a`    | 1×     | `A`         |
| 1     | `b`    | 2×     | `Bb`        |
| 2     | `c`    | 3×     | `Ccc`       |
| 3     | `d`    | 4×     | `Dddd`      |

Join with hyphens: `A-Bb-Ccc-Dddd`

## Insight

For each index `i`, repeat the character `i + 1` times, then capitalize (first letter upper, rest lower). Join the parts with `-`, or build the string and drop the trailing hyphen:

```text
(letter * (i + 1)).capitalize()
```
