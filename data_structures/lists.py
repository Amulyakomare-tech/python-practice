"""
LISTS IN PYTHON

A list is an ordered, mutable collection of items.
Lists can store multiple data types.
"""

# -----------------------------------
# 1️⃣ Creating Lists
# -----------------------------------

numbers = [1, 2, 3, 4, 5]
mixed = [10, "Python", 3.5, True]

print(numbers)
print(mixed)


# -----------------------------------
# 2️⃣ Accessing List Elements
# -----------------------------------

fruits = ["apple", "banana", "mango"]

print(fruits[0])     # first element
print(fruits[-1])    # last element


# -----------------------------------
# 3️⃣ List Slicing
# -----------------------------------

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])


# -----------------------------------
# 4️⃣ Modifying List Elements
# -----------------------------------

fruits = ["apple", "banana", "mango"]

fruits[1] = "orange"

print(fruits)


# -----------------------------------
# 5️⃣ Adding Elements
# -----------------------------------

numbers = [1, 2, 3]

numbers.append(4)      # add at end
numbers.insert(1, 10)  # insert at index

print(numbers)


# -----------------------------------
# 6️⃣ Removing Elements
# -----------------------------------

items = [10, 20, 30, 40]

items.remove(20)
items.pop()

print(items)


# -----------------------------------
# 7️⃣ Looping Through a List
# -----------------------------------

numbers = [5, 10, 15, 20]

for num in numbers:
    print(num)


# -----------------------------------
# 8️⃣ List Length
# -----------------------------------

data = [1, 2, 3, 4, 5]

print("Length:", len(data))"""
