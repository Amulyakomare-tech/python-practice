"""
USER INPUT IN PYTHON
"""

# -------------------
# 🔹 CONCEPT
# -------------------
# input() function is used to take input from user.
# By default input() returns data as string.
# We need type casting if we want numbers.

# -------------------
# 🔹 EXAMPLES
# -------------------

name = input("Enter your name: ")
print("Hello", name)

age = input("Enter your age: ")
print("Type of age:", type(age))  # always string

# Convert to int
age = int(age)
print("Age after conversion:", age)
print("Type after conversion:", type(age))


# -------------------
# 🔹 PRACTICE
# -------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result = num1 + num2
print("Sum is:", sum_result)

year = int(input("Enter your birth year: "))
current_year = 2025
print("You are", current_year - year, "years old")