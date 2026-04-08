"""
DECORATORS IN PYTHON (INTRODUCTION)

A decorator is a function that modifies the behavior of another function.
"""

# -----------------------------------
# 1️⃣ Basic Function
# -----------------------------------

def greet():
    print("Hello, welcome!")

greet()


# -----------------------------------
# 2️⃣ Function Inside Function
# -----------------------------------

def outer():
    def inner():
        print("Inside inner function")
    inner()

outer()


# -----------------------------------
# 3️⃣ Passing Function as Argument
# -----------------------------------

def greet():
    print("Hello!")

def display(func):
    func()

display(greet)


# -----------------------------------
# 4️⃣ Simple Decorator
# -----------------------------------

def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper


@my_decorator
def say_hello():
    print("Hello, Amulya!")

say_hello()


# -----------------------------------
# 5️⃣ Decorator with Parameters
# -----------------------------------

def decorator(func):
    def wrapper(name):
        print("Welcome message:")
        func(name)
        print("Goodbye message")
    return wrapper


@decorator
def greet_user(name):
    print(f"Hello {name}")

greet_user("Amulya")