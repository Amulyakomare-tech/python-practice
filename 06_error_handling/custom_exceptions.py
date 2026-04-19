"""
CUSTOM EXCEPTIONS IN PYTHON

We can create our own exceptions by inheriting from the Exception class.
"""

# -----------------------------------
# 1️⃣ Creating a Custom Exception
# -----------------------------------

class InvalidAgeError(Exception):
    """Custom exception for invalid age"""
    pass


# -----------------------------------
# 2️⃣ Using Custom Exception
# -----------------------------------

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    else:
        print("Access Granted")

try:
    check_age(16)
except InvalidAgeError as e:
    print("Error:", e)


# -----------------------------------
# 3️⃣ Another Example
# -----------------------------------

class InsufficientBalanceError(Exception):
    """Custom exception for low balance"""
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Not enough balance")
    else:
        print("Withdrawal successful")

try:
    withdraw(1000, 1500)
except InsufficientBalanceError as e:
    print("Error:", e)