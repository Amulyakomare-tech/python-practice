"""
INHERITANCE IN PYTHON

Inheritance allows one class to use properties and methods of another class.
"""

# -----------------------------------
# 1️⃣ Parent Class
# -----------------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")


# -----------------------------------
# 2️⃣ Child Class (Inheritance)
# -----------------------------------

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def show(self):
        print(f"Course: {self.course}")


student1 = Student("Amulya", "BCA")

student1.display()   # inherited method
student1.show()


# -----------------------------------
# 3️⃣ Method Overriding
# -----------------------------------

class Person:
    def display(self):
        print("This is Person class")


class Student(Person):
    def display(self):
        print("This is Student class")


obj = Student()
obj.display()


# -----------------------------------
# 4️⃣ Multiple Inheritance
# -----------------------------------

class Father:
    def skill1(self):
        print("Driving")


class Mother:
    def skill2(self):
        print("Cooking")


class Child(Father, Mother):
    pass


child = Child()
child.skill1()
child.skill2()