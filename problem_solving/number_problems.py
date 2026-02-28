"""
NUMBER BASED PROBLEMS
"""

# -----------------------
# Problem 1: Check Even or Odd
# -----------------------

num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# -----------------------
# Problem 2: Find Largest of Three Numbers
# -----------------------

a = 10
b = 25
c = 15

largest = max(a, b, c)
print("Largest number is:", largest)


# -----------------------
# Problem 3: Reverse a Number
# -----------------------

number = 1234
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reversed number:", reverse)
