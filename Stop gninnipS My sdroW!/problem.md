# Stop gninnipS My sdroW!

Given a string of one or more words, reverse every word that has **five or more letters**. Shorter words stay as they are.

The input contains only letters and spaces. Spaces appear only when there is more than one word.

```text
spin_words("Hey fellow warriors")  # → "Hey wollef sroirraw"
spin_words("This is a test")       # → "This is a test"
spin_words("This is another test") # → "This is rehtona test"
```

## Example

`spin_words("Hey fellow warriors")`

| Word     | Letters | Reversed? | Result    |
|----------|---------|-----------|-----------|
| Hey      | 3       | no        | `Hey`     |
| fellow   | 6       | yes       | `wollef`  |
| warriors | 8       | yes       | `sroirraw`|

Join with spaces: `Hey wollef sroirraw`

## Insight

Split on spaces, reverse a word only when its length is at least 5, then join:

```text
len(word) >= 5  →  word[::-1]
otherwise       →  word
```

A 4-letter word is left unchanged.
