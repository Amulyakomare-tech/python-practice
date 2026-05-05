"""
OPERATORS IN PYTHON
"""

# -----------------------
# 🔹 CONCEPT
# -----------------------
# Operators are used to perform operations on variables and values.
# Types:
# 1. Arithmetic
# 2. Comparison
# 3. Logical
# 4. Assignment

# -----------------------
# 🔹 ARITHMETIC OPERATORS
# -----------------------

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

# -----------------------
# 🔹 COMPARISON OPERATORS
# -----------------------

print(a > b)
print(a < b)
print(a == b)
print(a != b)

# -----------------------
# 🔹 LOGICAL OPERATORS
# -----------------------

x = 5
print(x > 2 and x < 10)
print(x > 2 or x > 10)
print(not(x > 2))

# -----------------------
# 🔹 PRACTICE
# -----------------------

num = 25

if num % 5 == 0 and num % 3 == 0:
    print("Divisible by both 5 and 3")
else:
    print("Not divisible by both")