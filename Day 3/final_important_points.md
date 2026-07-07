# 🐍 Day 3 – Conditional Statements

## 📚 Concepts

### Conditional Statements
- `if`
- `if-else`
- `if-elif-else`
- Nested `if`

### Other Topics
- Indentation
- Truthy & Falsy Values
- Ternary Operator

---

## ⭐ Important Points

- `if` checks the first condition.
- `elif` checks the next condition only if the previous one is False.
- `else` runs when all previous conditions are False.
- Python executes only the **first True** condition in an `if-elif-else` chain.
- Indentation defines code blocks in Python.
- `if` can have multiple `elif` blocks.
- `else` cannot exist without an `if`.
- Ternary Operator:
  ```python
  "Adult" if age >= 18 else "Minor"
  ```
- Falsy values:
  - `False`
  - `0`
  - `0.0`
  - `""`
  - `[]`
  - `{}`
  - `None`

---

## ❌ My Mistakes

- Thought indentation was related to time complexity.
- Forgot that after one `if` condition is True, Python skips all remaining `elif` blocks.
- Used `max()` first for the largest number question (good for Python, but not for interview logic).
- ATM project had an infinite loop when age was negative.
- Forgot to ask for Aadhaar input again after an invalid value.

---

## ✅ Improvements

- Explain concepts more precisely in interview answers.
- Handle invalid inputs before the main logic.
- Think about edge cases (negative numbers, equal values, invalid choices).
- For interview questions, solve with logic first, then use built-in functions.
- Use `>=` or handle equality explicitly when required.
- Keep improving programs after making them work.

---

## 🎯 Interview Questions

✔ Difference between `if`, `elif`, and `else`

✔ What is Nested `if`?

✔ Why is indentation important?

✔ What are Truthy and Falsy values?

✔ What is the ternary operator?

✔ Can `else` exist without `if`?

✔ Can `if` have multiple `elif` blocks?