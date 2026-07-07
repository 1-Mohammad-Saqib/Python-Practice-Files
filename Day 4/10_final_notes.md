# 🐍 Day 4 – Loops

## 📚 Concepts

### while Loop
- Runs while the condition is `True`.
- Best when the number of iterations is unknown.

### for Loop
- Used when the number of iterations is known.
- Commonly used with `range()`.

### range()
- `range(stop)`
- `range(start, stop)`
- `range(start, stop, step)`
- **Stop value is excluded.**

### Loop Control Statements
- `break` → Stops the loop.
- `continue` → Skips the current iteration.
- `pass` → Placeholder, does nothing.

### Nested Loops
- A loop inside another loop.
- Mostly used for patterns and matrices.

---

## ⭐ Important Points

- `while` → Unknown number of repetitions.
- `for` → Known number of repetitions.
- `range(5)` → `0 1 2 3 4`
- `range(1,10)` → `1 2 3 4 5 6 7 8 9`
- `break` exits the loop immediately.
- `continue` skips only the current iteration.
- `pass` does nothing.
- A variable declared **inside** a loop is recreated every iteration.
- A variable declared **outside** a loop keeps its value.

### Counter vs Accumulator

Counter

```python
count += 1
```

Accumulator

```python
total += value
```

---

## ❌ My Mistakes

- Forgot that `break` executes before `print()`.
- Thought `range()` includes the stop value.
- Didn't know `for` can iterate over strings and lists without `range()`.
- Used `sum` as a variable name (shadows Python's built-in `sum()` function).
- VS Code suggested the pattern solution before I could solve it.

---

## ✅ Improvements

- Use `total` instead of `sum`.
- Think about where variables should be declared (inside vs outside loops).
- Use counters for counting events.
- Use accumulators for adding values.
- Predict the output before running the code.
- Solve interview questions without using built-in shortcuts first.

---

## 🎯 Interview Questions

✔ Difference between `for` and `while`

✔ Difference between `break`, `continue`, and `pass`

✔ What is an infinite loop?

✔ Why doesn't `range(5)` include `5`?

✔ Can a `for` loop work without `range()`?

✔ What is a nested loop?

✔ Difference between a counter and an accumulator?
