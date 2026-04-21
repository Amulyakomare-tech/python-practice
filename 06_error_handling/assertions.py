"""
ASSERTIONS IN PYTHON

Assertions are used to test if a condition is true.
If the condition is false, an AssertionError is raised.
"""

# -----------------------------------
# 1️⃣ Basic Assertion
# -----------------------------------

x = 10

assert x > 0
print("x is positive")


# -----------------------------------
# 2️⃣ Assertion with Message
# -----------------------------------

age = 16

assert age >= 18, "Age must be at least 18"
print("Access granted")


# -----------------------------------
# 3️⃣ Using Assertion in Function
# -----------------------------------

def divide(a, b):
    """Divides two numbers"""
    assert b != 0, "Cannot divide by zero"
    return a / b

print(divide(10, 2))


# -----------------------------------
# 4️⃣ Debugging Example
# -----------------------------------

numbers = [1, 2, 3, 4]

assert len(numbers) == 4, "List length mismatch"

print("List length is correct")