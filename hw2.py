# Algo Questions
# Question 1
def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total

# Question 2
def half_list(lst):
    result = []
    for i in range(len(lst)):
        if i % 2 == 0:  # אם האינדקס זוגי
            result.append(lst[i])
    return result

# Question 3
def pyramid(n):
    for i in range(1, n + 1):
        print([i] * i)

# Question 4
def flipped_pyramid(n):
    for i in range(n, 0, -1):
        print('*' * i)

# Question 5a
def min_len(strings):
    if not strings:
        return ""
    shortest = strings[0]
    for s in strings[1:]:
        if len(s) < len(shortest):
            shortest = s
    return shortest

# Question 5b
def sort_str(strings):
    return sorted(strings, key=len)
# Or =>
def sort_str(strings):
    for i in range(len(strings)):
        min_index = i
        for j in range(i + 1, len(strings)):
            if len(strings[j]) < len(strings[min_index]):
                min_index = j
        # החלפת מקומות
        strings[i], strings[min_index] = strings[min_index], strings[i]
    return strings

# Question 6
def b_language(text):
    vowels = "aeiou"
    result = ""
    for char in text:
        result += char
        if char in vowels:
            result += "b" + char
    return result

# Question 7
def multiply(n):
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        print(row)

