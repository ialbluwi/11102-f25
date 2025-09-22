---
layout: page
title:  October 12
nav_exclude: true
author: Ibrahim Albluwi
---

# **2.** Conditionals 1
<span style="font-size: 0.8em; font-weight: normal; color: gray;">For October 12, 2025</span>

## Suggested Teaching Method
- Use interactive **live coding**. Alternate between the python `REPL` and writing programs in files depending on the number of lines.
- Use **predict-run-explain** instead of **explain-then-show**. I.e., show the code, ask them to predict the output, run the code, and then discuss why the output is what it is. There is empirical evidence showing that this is better than explaining something then demonstrating it. However, use wise judgement (depending on the example and the time available) for when to use what.

## Things To Cover 
1. **Boolean Expressions & Logical Operators**.
    - `==`, `!=`, `<`, `>`, `<=`, `>=`.
    <br>Ignore `is` and `is not` for now.
    - `and`, `or`, `not`.
    - Everything except the integer `0` and the float `0.0` is considered true (e.g., `17 and True`).

2. **Conditionals**.
    - Basic Syntax: <br>
    ```python
    if CONDITION:
        STATEMENT_1
        STATEMETN_2
    ```
    - Indentation:
    ```python
    x = int(input())
    y = int(input())
    if x > y:
        print('Aha!')
        print('Ha Ha!')
    ```
    vs
    ```python
    x = int(input())
    y = int(input())
    if x > y:
        print('Aha!')
    print('Ha Ha!')
    ```
    Show also that an unexpected indentation leads to an error. E.g.,
    ```
    >>>   x = 1
    IndentationError: unexpected indent
    ```
    - `else`. Use a simple example.
    - `elif`. Use a simple example.
3. **Others**.
    - Show basic nested statements (depending on time). The following lecture will have a lot of nesting.
    - Ignore catching exceptions.
    - Short Circuiting.<br>
    ```python
    if x != 0 and (y / x) < 1:
        print('fraction')
    # vs
    if (y / x) < 1 and x != 0:
        print('fraction')
    ```