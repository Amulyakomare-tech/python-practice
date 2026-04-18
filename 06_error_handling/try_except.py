"""
ERROR HANDLING IN PYTHON

Used to handle runtime errors and prevent program crashes.
"""

# -----------------------------------
# 1️⃣ Basic try-except
# -----------------------------------

try:
    num = int(input("Enter a number: "))
    print("Number:", num)
except:
    print("Invalid input!")


# -----------------------------------
# 2️⃣ Specific Exception
# -----------------------------------

try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")


# -----------------------------------
# 3️⃣ Multiple Exceptions
# -----------------------------------

try:
    num = int("abc")
except ValueError:
    print("ValueError occurred")
except TypeError:
    print("TypeError occurred")


# -----------------------------------
# 4️⃣ else Block
# -----------------------------------

try:
    num = int("10")
except ValueError:
    print("Error")
else:
    print("No error, number is:", num)


# -----------------------------------
# 5️⃣ finally Block
# -----------------------------------

try:
    print("Trying...")
except:
    print("Error")
finally:
    print("This always executes")
