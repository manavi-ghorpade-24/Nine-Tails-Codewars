# Directions Reduction

You are given a list of directions: `"NORTH"`, `"SOUTH"`, `"EAST"`, `"WEST"`.

Going one way and immediately the opposite is wasted effort. Reduce the path by cancelling adjacent opposites:

- `NORTH` ↔ `SOUTH`
- `EAST` ↔ `WEST`

Cancellations can chain: after a pair disappears, new neighbors may also be opposites.

Return the simplified list. If everything cancels, return `[]`.

```text
dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])  # → ["WEST"]
dir_reduc(["NORTH", "SOUTH", "EAST", "WEST"])                           # → []
dir_reduc(["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"])           # → ["WEST", "WEST"]
dir_reduc(["NORTH", "WEST", "SOUTH", "EAST"])                           # → ["NORTH", "WEST", "SOUTH", "EAST"]
```

## Example

`["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]`

| Step | Path                                      | What happens        |
|------|-------------------------------------------|---------------------|
| 1    | `NORTH SOUTH …`                           | N and S cancel      |
| 2    | `SOUTH EAST WEST NORTH WEST`              | E and W cancel      |
| 3    | `SOUTH NORTH WEST`                        | S and N cancel      |
| 4    | `WEST`                                    | done                |

Not every path shrinks. In `["NORTH", "WEST", "SOUTH", "EAST"]` no two **adjacent** directions are opposites, so the result is the path itself.

## Insight

Walk the list with a stack. For each direction, if it is the opposite of the top of the stack, pop; otherwise push:

```text
opposite of stack top  →  pop
otherwise              →  push
```

The stack is the reduced path.
