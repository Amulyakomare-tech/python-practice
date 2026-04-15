"""
MAGIC METHODS (DUNDER METHODS) IN PYTHON

Magic methods are special methods with double underscores (__).
They allow us to define behavior for built-in operations.
"""

# -----------------------------------
# 1️⃣ __init__ (Constructor)
# -----------------------------------

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Amulya")
print(s1.name)


# -----------------------------------
# 2️⃣ __str__ (String Representation)
# -----------------------------------

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student Name: {self.name}"

s1 = Student("Amulya")
print(s1)


# -----------------------------------
# 3️⃣ __len__ (Length)
# -----------------------------------

class MyList:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

obj = MyList([1, 2, 3, 4])
print(len(obj))


# -----------------------------------
# 4️⃣ __add__ (Operator Overloading)
# -----------------------------------

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)


# -----------------------------------
# 5️⃣ __eq__ (Comparison)
# -----------------------------------

class Person:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

p1 = Person(20)
p2 = Person(20)

print(p1 == p2)