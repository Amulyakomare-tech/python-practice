"""
TUPLES IN PYTHON

A tuple is an ordered and immutable collection of items.
Once created, tuple elements cannot be changed.
"""

# -----------------------------------
# 1️⃣ Creating Tuples
# -----------------------------------

numbers = (1, 2, 3, 4)
mixed = (10, "Python", 3.5)

print(numbers)
print(mixed)


# -----------------------------------
# 2️⃣ Accessing Tuple Elements
# -----------------------------------

fruits = ("apple", "banana", "mango")

print(fruits[0])      # first element
print(fruits[-1])     # last element


# -----------------------------------
# 3️⃣ Tuple Slicing
# -----------------------------------

data = (10, 20, 30, 40, 50)

print(data[1:4])
print(data[:3])
print(data[2:])


# -----------------------------------
# 4️⃣ Tuple Length
# -----------------------------------

numbers = (5, 10, 15, 20)

print("Length:", len(numbers))


# -----------------------------------
# 5️⃣ Looping Through a Tuple
# -----------------------------------

colors = ("red", "green", "blue")

for color in colors:
    print(color)


# -----------------------------------
# 6️⃣ Tuple Packing & Unpacking
# -----------------------------------

person = ("Amulya", 20, "Student")

name, age, profession = person

print(name)
print(age)
print(profession)