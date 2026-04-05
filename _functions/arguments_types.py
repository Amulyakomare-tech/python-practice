"""
TYPES OF FUNCTION ARGUMENTS IN PYTHON

Different ways to pass arguments to functions:
- Positional Arguments
- Keyword Arguments
- Default Arguments
- *args
- **kwargs
"""

# -----------------------------------
# 1️⃣ Positional Arguments
# -----------------------------------

def add(a, b):
    """Adds two numbers"""
    return a + b

print(add(5, 10))


# -----------------------------------
# 2️⃣ Keyword Arguments
# -----------------------------------

def student(name, age):
    """Displays student info"""
    print(f"Name: {name}, Age: {age}")

student(name="Amulya", age=20)


# -----------------------------------
# 3️⃣ Default Arguments
# -----------------------------------

def greet(name="Guest"):
    """Greets user with default name"""
    print("Hello,", name)

greet()
greet("Amulya")


# -----------------------------------
# 4️⃣ *args (Multiple Positional Arguments)
# -----------------------------------

def sum_all(*numbers):
    """Returns sum of all numbers"""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3, 4))


# -----------------------------------
# 5️⃣ **kwargs (Multiple Keyword Arguments)
# -----------------------------------

def display_info(**data):
    """Displays key-value pairs"""
    for key, value in data.items():
        print(key, ":", value)

display_info(name="Amulya", age=20, course="BCA")