"""
ENCAPSULATION IN PYTHON

Encapsulation means restricting direct access to data
and controlling it using methods.
"""

# -----------------------------------
# 1️⃣ Public Variable
# -----------------------------------

class Student:
    def __init__(self, name):
        self.name = name   # public

student = Student("Amulya")
print(student.name)


# -----------------------------------
# 2️⃣ Protected Variable (_)
# -----------------------------------

class Student:
    def __init__(self, name):
        self._name = name   # protected

student = Student("Amulya")
print(student._name)


# -----------------------------------
# 3️⃣ Private Variable (__)
# -----------------------------------

class Student:
    def __init__(self, name):
        self.__name = name   # private

    def get_name(self):
        return self.__name


student = Student("Amulya")
print(student.get_name())

# print(student.__name)  ❌ will give error


# -----------------------------------
# 4️⃣ Getter and Setter Methods
# -----------------------------------

class BankAccount:
    def __