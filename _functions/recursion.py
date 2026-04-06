"""
RECURSION IN PYTHON

Recursion is when a function calls itself.
Used to solve problems by breaking them into smaller subproblems.
"""

# -----------------------------------
# 1️⃣ Basic Example
# -----------------------------------

def countdown(n):
    """Prints numbers from n to 1"""
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)


# -----------------------------------
# 2️⃣ Factorial Using Recursion
# -----------------------------------

def factorial(n):
    """Returns factorial of a number"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


# -----------------------------------
# 3️⃣ Sum of Numbers Using Recursion
# -----------------------------------

def sum_n(n):
    """Returns sum of first n numbers"""
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print("Sum:", sum_n(5))


# -----------------------------------
# 4️⃣ Fibonacci Using Recursion
# -----------------------------------

def fibonacci(n):
    """Returns nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci:", fibonacci(6))