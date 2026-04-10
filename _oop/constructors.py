"""
CONSTRUCTORS IN PYTHON

A constructor is a special method used to initialize objects.
In Python, it is defined using __init__().
"""

# -----------------------------------
# 1️⃣ Basic Constructor
# -----------------------------------

class Student:
    def __init__(self):
        print("Constructor called")

student1 = Student()


# -----------------------------------
# 2️⃣ Constructor with Parameters
# -----------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Amulya", 20)

print(student1.name)
print(student1.age)


# -----------------------------------
# 3️⃣ Using Constructor with Method
# -----------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

student1 = Student("Amulya", 20)
student1.display()


# -----------------------------------
# 4️⃣ Default Values in Constructor
# -----------------------------------

class Student:
    def __init__(self, name="Guest", age=18):
        self.name = name
        self.age = age

student1 = Student()
student2 = Student("Amulya", 20)

print(student1.name, student1.age)
print(student2.name, student2.age)