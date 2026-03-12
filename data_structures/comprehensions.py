"""
COMPREHENSIONS IN PYTHON

Comprehensions provide a concise way to create collections.
Common types:
- List Comprehension
- Set Comprehension
- Dictionary Comprehension
"""

# -----------------------------------
# 1️⃣ List Comprehension
# -----------------------------------

# Traditional way
squares = []

for i in range(1, 6):
    squares.append(i * i)

print("Traditional:", squares)

# Using list comprehension
squares_comp = [i * i for i in range(1, 6)]

print("List Comprehension:", squares_comp)


# -----------------------------------
# 2️⃣ List Comprehension with Condition
# -----------------------------------

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [n for n in numbers if n % 2 == 0]

print("Even Numbers:", even_numbers)


# -----------------------------------
# 3️⃣ Set Comprehension
# -----------------------------------

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_squares = {n * n for n in numbers}

print("Set Comprehension:", unique_squares)


# -----------------------------------
# 4️⃣ Dictionary Comprehension
# -----------------------------------

numbers = [1, 2, 3, 4]

square_dict = {n: n * n for n in numbers}

print("Dictionary Comprehension:", square_dict)