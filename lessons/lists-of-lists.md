---
layout: page
title:  Nov 18
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

# Lists of Lists

A list can contain elements of any type as elements, including other lists. When a list contains other lists as elements, it is often referred to as a _list of lists_. If each row in the list has the same number of elements, it is called a _2D list_ (two-dimensional list).

## Example: Creating and Accessing a List of Lists

Here is a simple example showing how to create and access elements in a list of lists:

```python
matrix = [[1, 2, 3, 4],
          [5, 6, 6, 7],
          [7, 8, 9, 10]]

print(matrix[0])    # Prints the first row [1, 2, 3, 4]
print(matrix[2])    # Prints the last row  [7, 8, 9, 10]

print(len(matrix))     # Prints the number of rows: 3
print(len(matrix[0]))  # Prints the number of columns 
                       # in the first row: 4

print(matrix[1][2])  # Prints the element at
                     # row 1, column 2: 6
print(matrix[2][3])  # Prints the element at
                     # row 2, column 3: 10

# print the element in the last row and last column
rows = len(matrix)
cols = len(matrix[0])
print(matrix[rows-1][cols-1])  # Output: 10
```

To print the 2D list, we can use `print(matrix)`, but it will print all the rows in a single line, which may not be very readable. Instead, we can use a loop to print each row on a separate line:

```python
def print_2D(matrix):
    for row in matrix:
        print(row)
```

## Creating a 2D List Dynamically

The above example shows how to create a 2D list with hardcoded values. However, in many cases, you may want to create a 2D list dynamically based on user input or other data. 

Let's begin by creating a 2D list with a specified number of rows and columns, initializing all elements to zero:

```python
rows = 3
cols = 4
matrix = []
for i in range(rows):
    row = [0] * cols    # Create a row with cols zeros
    matrix.append(row)  # Add the row to the matrix
```

This is more tedious than creating a 1D list. Therefore, we can create a helper function that we can reuse whenever we need to create a 2D list:

```python
def create_2D(rows, cols, value):
    matrix = []
    for i in range(rows):
        row = [value] * cols
        matrix.append(row)
    return matrix
```

We can now use this function to create a 2D list of any size, initialized with any value:

```python
matrix = create_2D(3, 4, 0)  # Creates a 3x4 matrix filled with zeros
print_2D(matrix)

# Output:
# [0, 0, 0, 0]
# [0, 0, 0, 0]
# [0, 0, 0, 0]

matrix = create_2D(2, 5, -1)  # Creates a 2x5 matrix filled with -1
print_2D(matrix)

# Output:
# [-1, -1, -1, -1, -1]
# [-1, -1, -1, -1, -1]
```

## Exercise 1

Define a function that receives a 2D list and prints each row on a separate line along with the sum of the elements in that row.

### Solution

```python
def print_rows_with_sums(matrix):
    for row in matrix:
        row_sum = sum(row)
        print(row, "Sum:", row_sum)

matrix = create_2D(3, 4, 1)
print_rows_with_sums(matrix)

# Output:
# [1, 1, 1, 1] Sum: 4
# [1, 1, 1, 1] Sum: 4
# [1, 1, 1, 1] Sum: 4
```

## Exercise 2

Define a function that receives a 2D list and fills it with random integers between 0 and 9.

### Solution

```python
import random

def fill_2D_with_random(matrix):
    for row in matrix:
        for i in range(len(row)):
            row[i] = random.randint(0, 9)

matrix = create_2D(3, 4, 0)
fill_2D_with_random(matrix)
print_2D(matrix)
```

Here is an alternative implementation that uses indices to access elements:

```python
def fill_2D_with_random(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = random.randint(0, 9)
```
        

## Exercise 3

Define a function that receives a non-empty 2D list and prints the average of all its elements.

### Solution

Below are three different implementations of the function. Familiarize yourself with all of them.

```python
# MAIN LOGIC: For every row: Go through every value 
# in the row, add it to total, and increment count.

def average_2D(matrix):
    total = 0
    count = 0
    for row in matrix:
        for value in row:
            total += value
            count += 1

    return total / count
```

```python
# MAIN LOGIC: For every row: Sum the row and add to 
# total, increment count by length of the row.

def average_2D(matrix):
    total = 0
    count = 0
    for row in matrix:
        total += sum(row)
        count += len(row)

    return total / count
```

```python
# MAIN LOGIC: For every row index r and column index c:
# Add matrix[r][c] to total, and increment count.

def average_2D(matrix):
    N = len(matrix)     # number of rows
    M = len(matrix[0])  # number of columns

    total = 0
    count = 0
    for r in range(N):
        for c in range(M):
            total += matrix[r][c]
            count += 1

    return total / count
```

## Exercise 4

Define a function that receives a 2D list and a column index, and returns the sum of the elements in that column. You can assume that the column index is valid (i.e., it is between `0` and the number of columns minus one).

### Solution

```python
def column_sum(matrix, c):
    total = 0
    for row in matrix:
        total += row[c]
    return total
```

## Exercise 5

Define a function that receives a 2D list and prints the sum of each column.

### Solution

We can reuse the same logic as in Exercise 4, but this time we will loop through all column indices.

```python
def column_sums(matrix):
    N = len(matrix)     # number of rows
    M = len(matrix[0])  # number of columns

    for c in range(M):
        total = 0
        for row in matrix:
            total += row[c]
        print("Sum of column", c, "is", total)
```

Here is an alternative implementation that uses row and column indices to access elements:

```python
def column_sums(matrix):
    N = len(matrix)     # number of rows
    M = len(matrix[0])  # number of columns

    for c in range(M):
        total = 0
        for r in range(N): 
            total += matrix[r][c]
        
        print("Sum of column", c, "is", total)
```
