"""
FUNCTIONS IN PYTHON

A function is a block of reusable code that performs a specific task.
"""

# -----------------------------------
# 1️⃣ Defining a Function
# -----------------------------------

def greet():
    print("Hello, welcome to Python!")

greet()


# -----------------------------------
# 2️⃣ Function with Parameters
# -----------------------------------

def greet_user(name):
    print("Hello,", name)

greet_user("Amulya")


# -----------------------------------
# 3️⃣ Function with Return Value
# -----------------------------------

def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)


# -----------------------------------
# 4️⃣ Default Parameters
# -----------------------------------

def greet(name="Guest"):
    print("Hello,", name)

greet()
greet("Amulya")


# -----------------------------------
# 5️⃣ Multiple Parameters
# -----------------------------------

def student_info(name, age, course):
    print(f"Name: {name}, Age: {age}, Course: {course}")

student_info("Amulya", 20, "BCA")
