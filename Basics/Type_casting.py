"""
Type Casting and User Input in Python
Practice examples to understand data conversion and input handling.
"""

# --- Type Casting ---

age = "20"
print("Before type casting:", type(age))

age = int(age)
print("After type casting:", type(age))


number = 10
number = float(number)
print("Converted to float:", number)


# --- User Input ---

name = input("Enter your name: ")
print("Hello,", name)

birth_year = input("Enter your birth year: ")
birth_year = int(birth_year)

current_year = 2025
age = current_year - birth_year

print("You are", age, "years old.")