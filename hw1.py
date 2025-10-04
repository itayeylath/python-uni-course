# Question 1
def min_list2(l1, l2):
    if len(l1) < len(l2):
        return l1
    return l2  # No need for else because if the first condition is True, we won't reach this line


# Question 2
def count_in_list(lst, x):
    count = 0
    for element in lst:
        if element == x:
            count = count + 1
    return count


# Question 7
def count_in_list2(lst, x):
    count = 0
    i = 0  # Start with the first index
    while i < len(lst):  # As long as i is a valid index
        if lst[i] == x:
            count = count + 1
        i = i + 1  # Move to the next index
    return count


# Question 3
def count_even_in_list(lst):
    count = 0
    for i in lst:
        if i % 2 == 0:
            count = count + 1
    return count


# Question 4
def min_list_even(l1, l2):
    if count_even_in_list(l1) < count_even_in_list(l2): # Here I use the function from Question 3
        return l1
    return l2


# Question 5
def factorial(n):
    x = 1
    for i in range(2, n + 1):
        x = x * i
    return x


# Question 6
def odd_factorial(n):
    x = 1
    for i in range(2, n + 1):
        if i % 2 == 1:
            x = x * i
    return x


# Question 8
def odd_factorial2(n):
    x = 1
    i = 1
    while i <= n:
        if i % 2 == 1:  # Check if i is odd
            x = x * i
        i = i + 1

    return x


# Question 9
def inverse_sum(n):
    i = 1
    total = 1
    while total <= n:   # Keep adding until the total is bigger than n
        i = i + 1
        total = total + i
    return i - 1


# Question 10
def inverse_odd_factorial(n):
    i = 1
    while odd_factorial(i) <= n:   # Keep checking odd factorial until it is bigger than n
        i = i + 1
    return i - 1
