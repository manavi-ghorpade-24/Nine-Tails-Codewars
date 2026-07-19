# Alphabet War — Airstrike — Letters Massacre

There is a war between two sides of the alphabet. The fight string is lowercase letters plus `*`, each `*` a bomb. Bombs explode first: a `*` destroys itself and the letters **immediately next to it**. Then the surviving letters score, and the higher total wins.

```text
alphabet_war("s*zz")           # → "Right side wins!"
alphabet_war("*zd*qm*wp*bs*")  # → "Let's fight again!"
alphabet_war("zzzz*s*")        # → "Right side wins!"
alphabet_war("www*www****z")   # → "Left side wins!"
```

## Powers

| Left | Power | Right | Power |
|------|-------|-------|-------|
| `w`  | 4     | `m`   | 4     |
| `p`  | 3     | `q`   | 3     |
| `b`  | 2     | `d`   | 2     |
| `s`  | 1     | `z`   | 1     |

Any other letter has **no power** (it can still die in an airstrike). Bombs do not score.

## Outcome

| Result              | When                    |
|---------------------|-------------------------|
| `Left side wins!`   | left score > right      |
| `Right side wins!`  | right score > left      |
| `Let's fight again!`| scores are equal        |

## Example

`"s*zz"` → bombs kill `s` and the first `z`. One `z` survives (power 1). Right wins.

```text
s * z z
† † † z     →  right 1, left 0  →  "Right side wins!"
```

`aa*aa` becomes `a___a`: the `*` and both adjacent letters are gone.

## Insight

Walk the string once. A character is dead if the previous or next character is `*`. Only living letters that appear in a power map add to that side’s score.

```text
fight[i-1] == "*" or fight[i+1] == "*"  →  skip (dead)
otherwise, if letter in left/right map  →  add its power
```

Check both neighbors only when those indices exist (`i > 0`, `i < len(fight) - 1`). Then compare the two totals.
