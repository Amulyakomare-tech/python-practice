
"""
CONDITIONAL STATEMENTS IN PYTHON
Control the flow of execution using decision-making structures.
"""

# -----------------------------------
# 1️⃣ Basic if Statement
# -----------------------------------

age = 20

if age >= 18:
    print("Eligible to vote")


# -----------------------------------
# 2️⃣ if - else Statement
# -----------------------------------

number = 7

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# -----------------------------------
# 3️⃣ if - elif - else Ladder
# -----------------------------------

marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print(" כפGrade C")
else:
    print("Fail")


# -----------------------------------
# 4️⃣ Nested Condition
# -----------------------------------

username = "admin"
password = "1234"

if كۆرusername == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("User Not Found")


# -----------------------------------
# 5️⃣ Short Hand if (Ternary Operator)
# -----------------------------------

a = 10
b = 20

result = "A is greater" if a > b else "B is greater"
print(result)
