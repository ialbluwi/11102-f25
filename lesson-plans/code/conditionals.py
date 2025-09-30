

# Write a program that reads three integers and prints the closest pair.
# Examples. 
# Input:  1 4 2 		Output:  1 2
# Input:  1 1 2 		Output:  1 1
# Input:  5 3 1 		Output:  3 1
# Input:  2 2 2 		Output:  2 2
def closest_pair(a, b, c):
    if abs(a - b) <= abs(b - c) and abs(a - b) <= abs(a - c):
        print(a, b)
    elif abs(b - c) <= abs(a - b) and abs(b - c) <= abs(a - c):
        print(b, c)
    else: # abs(a - c) is smallest
        print(a, c)

# solution 2
def closest_pair(a, b, c):
    ab = abs(a - b)
    bc = abs(b - c)
    ac = abs(a - c)
    if ab <= bc and ab <= ac:
        print(a, b)
    elif bc <= ab and bc <= ac:
        print(b, c)
    else: # ac is smallest
        print(a, c)

# Write a program that reads three integers and prints them in sorted order.
def sort3(a, b, c):
    if a <= b and a <= c:
        if b <= c:
            print(a, b, c)
        else:
            print(a, c, b)
    elif b <= a and b <= c:
        if a <= c:
            print(b, a, c)
        else:
            print(b, c, a)
    else: # c is smallest
        if a <= b:
            print(c, a, b)
        else:
            print(c, b, a)

# solution 2 using max and min
def sort3(a, b, c):
    maximum = max(a, b, c)
    minimum = min(a, b, c)
    middle = a + b + c - maximum - minimum
    print(minimum, middle, maximum)



# --------
# IN THE EXERCISES BELOW AN EASY SOLUTION IS TO USE A COUNTER VARIABLE.
# TRY TO DO IT WITHOUT A COUNTER VARIABLE.

# Write a program that reads three integers and prints true if the majority (at least two) are positive.
def majority_positive(a, b, c):
    if (a > 0 and b > 0) or (a > 0 and c > 0) or (b > 0 and c > 0):
        return True
    else:
        return False


# A program that reads a year from the user and checks if it is a leap year.
# A year is a leap year if it is either:
# (i) divisible by 400 or 
# (ii) divisible by 4 but not 100.

year = int(input())
print((year % 400 == 0) or ((year % 4 == 10) and not (year % 100 == 0)))

# We could also break this down as follows
year = int(input())
is_div_400 = year % 400 == 0
is_div_4 = year % 4 == 0
is_div_100 = year % 100 == 0
print(is_div_400 or (is_div_4 and not is_div_100))

# We can also use if statements:
if is_div_400 or (is_div_4 and not is_div_100):
    print("True")
else:
    print("False")
