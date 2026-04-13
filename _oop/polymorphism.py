"""
POLYMORPHISM IN PYTHON

Polymorphism means "many forms".
Same method behaves differently depending on the object.
"""

# -----------------------------------
# 1️⃣ Method Overriding (Runtime Polymorphism)
# -----------------------------------

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# -----------------------------------
# 2️⃣ Same Function, Different Objects
# -----------------------------------

class Bird:
    def sound(self):
        print("Bird chirps")


class Lion:
    def sound(self):
        print("Lion roars")


def make_sound(animal):
    animal.sound()


make_sound(Bird())
make_sound(Lion())


# -----------------------------------
# 3️⃣ Built-in Polymorphism
# -----------------------------------

print(len("Python"))        # string length
print(len([1, 2, 3, 4]))    # list length


# -----------------------------------
# 4️⃣ Operator Polymorphism
# -----------------------------------

print(5 + 3)         # addition
print("Hello " + "World")   # string concatenation