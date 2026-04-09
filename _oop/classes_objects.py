"""
CLASSES AND OBJECTS IN PYTHON

Class = Blueprint
Object = Instance of class
"""

# -----------------------------------
# 1️⃣ Creating a Class
# -----------------------------------

class Student:
    pass


# -----------------------------------
# 2️⃣ Creating an Object
# -----------------------------------

student1 = Student()

print(student1)


# -----------------------------------
# 3️⃣ Class with Attributes
# -----------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Amulya", 20)

print(student1.name)
print(student1.age)


# -----------------------------------
# 4️⃣ Adding Methods
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
# 5️⃣ Multiple Objects
# -----------------------------------

student1 = Student("Amulya", 20)
student2 = Student("Rahul", 22)

student1.display()
student2.display()
