"""
LAMBDA FUNCTIONS IN PYTHON

A lambda function is a small anonymous function.
It can have multiple arguments but only one expression.
"""

# -----------------------------------
# 1️⃣ Basic Lambda Function
# -----------------------------------

# Normal function
def add(a, b):
    return a + b

# Lambda function
add_lambda = lambda a, b: a + b

print("Lambda Add:", add_lambda(5, 10))


# -----------------------------------
# 2️⃣ Lambda with Single Argument
# -----------------------------------

square = lambda x: x * x

print("Square:", square(6))


# -----------------------------------
# 3️⃣ Lambda with map()
# -----------------------------------

numbers = [1, 2, 3, 4]

squares = list(map(lambda x: x * x, numbers))

print("Squares using map:", squares)


# -----------------------------------
# 4️⃣ Lambda with filter()
# -----------------------------------

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even_numbers)


# -----------------------------------
# 5️⃣ Lambda with sorted()
# -----------------------------------

data = [(1, 3), (2, 1), (4, 2)]

sorted_data = sorted(data, key=lambda x: x[1])

print("Sorted by second element:", sorted_data)