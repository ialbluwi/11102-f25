---
layout: page
title:  November 4
nav_exclude: true
author: Ibrahim Albluwi
---

<style>
h2 {
    font-weight: 400;           /* normal weight, not bold */
    font-family: "Open Sans", sans-serif;  /* different font face */
    color: #3b7dc0ff;             /* optional: different color */
}
</style>

# Strings (Iteration & Manipulation)
<span style="font-size: 0.8em; font-weight: normal; color: gray;">Bisc syntax and examples.</span>

## Basic Iteration

The following three pieces of code all do the same thing (printing the characters of the string, each on a separate line). The first one is the easiest to use.

```python
course = 'Introduction'
for c in course:
    print(c)
```

```python
course = 'Introduction'
for i in range(len(course)):
    print(course[i])
```

```python
course = 'Introduction'
i = 0
while i < len(course):
    print(course[i])
    i += 1
```
---

## Debugging

The following code attempts to print the course name in reverse. However, it has bugs. What are they? 

```python
course = 'Introduction'
for i in range(len(course), 0, -1):
    print(course[i])
```

<details class="jtd-accordion">
  <summary>Answer</summary>
    <ul>
        <li> The range should start at <code>len(course) - 1</code>. Otherwise we will get an <code>IndexError</code>.</li>
        <li> The range should end at <code>-1</code>. Otherwise we will not see the character at index <code>0</code>.</li>
    </ul>
</details>

Note that the easiest way to iterate over the characters of the string in reverse order is as follows:
```python
for c in course[::-1]:
     print(c)
```

## Application 1: Palindromes

```python
def is_palindrome(s):
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True
```

**FOLLOW-UP QUESTION 1.** Can you write the above code using a for-loop?

**FOLLOW-UP QUESTION 2.** Can you write the above code using a single line?

## Application 2: Parsing Strings

```python
for i in range(1, 11):
    email = input("Enter your university email " + str(i) + ": ")
    pos1 = email.find('@')
    pos2 = email.find('.jo')

    if pos1 < 0 or pos2 < 0:
        print("ERROR: Invalid jordanian email")
        continue

    domain = email[pos1 + 1 : pos2]
    print("So you are from: ", domain, "!!!")
```