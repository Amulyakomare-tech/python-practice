"""
SETS IN PYTHON

A set is an unordered collection of unique elements.
Sets do not allow duplicate values.
"""

# -----------------------------------
# 1️⃣ Creating Sets
# -----------------------------------

numbers = {1, 2, 3, 4, 5}

print(numbers)


# -----------------------------------
# 2️⃣ Duplicate Values
# -----------------------------------

data = {1, 2, 2, 3, 3, 4}

print(data)  # duplicates automatically removed


# -----------------------------------
# 3️⃣ Adding Elements
# -----------------------------------

fruits = {"apple", "banana"}

fruits.add("mango")

print(fruits)


# -----------------------------------
# 4️⃣ Removing Elements
# -----------------------------------

fruits = {"apple", "banana", "mango"}

fruits.remove("banana")

print(fruits)


# -----------------------------------
# 5️⃣ Set Union
# -----------------------------------

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))


# -----------------------------------
# 6️⃣ Set Intersection
# -----------------------------------

print(set1.intersection(set2))


# -----------------------------------
# 7️⃣ Looping Through Set
# -----------------------------------

colors = {"red", "green", "blue"}

for color in colors:
    print(color)