# Create Phone Number

Write a function that accepts an array of **10 integers** (each between `0` and `9`) and returns those numbers as a phone-number string.

The returned format must be exact:

```text
"(XXX) XXX-XXXX"
```

There is a **space after the closing parenthesis**.

## Example

```text
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])  # → "(123) 456-7890"
```

| Digits                         | Result            |
|--------------------------------|-------------------|
| `[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]` | `(123) 456-7890` |

## Format

| Part        | Digits | Positions |
|-------------|--------|-----------|
| Area code   | 3      | `n[0:3]`  |
| Prefix      | 3      | `n[3:6]`  |
| Line number | 4      | `n[6:10]` |

```text
(  1  2  3  )   4  5  6  -  7  8  9  0
   └─area─┘     └prefix┘    └──line──┘
```

## Insight

Turn the ten digits into one string, then slice it into the three groups:

```text
digits = "1234567890"
"(" + digits[:3] + ") " + digits[3:6] + "-" + digits[6:]
```

`map(str, n)` converts each int to a character; `''.join(...)` concatenates them. An f-string then inserts the slices into the template.
