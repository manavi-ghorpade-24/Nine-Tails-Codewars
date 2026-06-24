# Friend or Foe?

Filter a list of names and keep only your friends. A name is a friend if and only if it has **exactly 4 letters**.

Keep the original order. Input strings contain letters only.

```text
friend(["Ryan", "Kieran", "Jason", "Yous"])  # → ["Ryan", "Yous"]
friend(["Peter", "Stephen", "Joe"])          # → []
```

## Example

| Name    | Letters | Friend? |
|---------|---------|---------|
| Ryan    | 4       | yes     |
| Kieran  | 6       | no      |
| Jason   | 5       | no      |
| Yous    | 4       | yes     |
| Peter   | 5       | no      |
| Stephen | 7       | no      |
| Joe     | 3       | no      |

## Insight

Walk the list once and keep names whose length is exactly 4:

```text
len(name) == 4  →  keep
otherwise       →  drop
```
