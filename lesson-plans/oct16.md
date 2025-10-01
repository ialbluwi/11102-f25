---
layout: page
title:  October 16
nav_exclude: true
author: Ibrahim Albluwi
---

# **6.** Functions 1
<span style="font-size: 0.8em; font-weight: normal; color: gray;">For October 16, 2025</span>

## Lecture Goals

This is the first of two lectures intended to introduce functions. In this lecture, we will cover:
- Basic terminology.
- Built-in functions.
- Syntax for defining and calling functions.

In the following lecture, we will delve more into issues like scope, call stacks, etc.

## Outline

Follow the outline of [P4E.4](https://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf#page=55.16). However, note the following:

- In **4.2**, you can use `max(1, 5, 0)` or `min(x, y, z)` (for example) instead of or with the examples used in the book. The book examples find the maximum and minimum characters in a string, which might not be clear to the students, given that they do not yet know that characters are represented as numbers (e.g. ASCII).

- In **4.5**, the book uses a `for` loop to show that calling `random.random()` multiple times gives different values. Do **NOT** use a `for` loop. Achieve the same thing by calling the function multiple times in the terminal.

- In **4.5**, instead of:
```python
>>> t = [1, 2, 3, 4]
>>> random.choice(t)
```
Use the following, which might save us the discussion on what lists are.
```python
>>> random.choice([1, 2, 3, 4])
```

- Emphasize the difference between:
    - Functions that are called using the module name like `random.random()` and `math.sqrt(2)`, and functions that are called directly like `max(...)`, `len(...)`, `print(...)`, etc.
    - Functions that require arguments like `max(...)`, `len(...)`, and `random.choice([...])` and functions that don't require arguments like `input()` and `random.random()`.
    - Functions that **return** values like `input()`, `max(...)`, and `len(...)` and functions that don't return values like `print(...)`.

- All of the above should take 10-20 minutes at most. The great majority of the lecture should focus on how to **define** new functions (4.6 - 4.11).


Here is one way to motivate why we need to **define** new functions. Ask them: 
> _Imagine if `print()` did not exist, and that every time you wanted to print something to the screen, you had to write from scratch all the complicated and long code that does the printing. Would that be convenient?_. 

Luckily, we only need to call the function. This saves time, makes our code shorter and more readable, and reduces the possibilities of making mistakes.

## Suggested Teaching method

Use the Python terminal (`REPL`) for showing built-in functions and then move to writing code in files when you discuss how to define a function. You can keep GitHub Copilot on to speed up writing the functions if you wish.


