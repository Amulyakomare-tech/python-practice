"""
NESTED STRUCTURES IN PYTHON

Nested structures mean using one control structure inside another.
Examples:
- Nested if statements
- Nested loops
"""

# -----------------------------------
# 1️⃣ Nested If Example
# -----------------------------------

print("Nested If Example:")

age = 22
citizenship = "India"

if age >= 18:
    if citizenship == "India":
        print("Eligible to vote")
    else:
        print("Citizenship required")
else:
    print("Not eligible to vote")


# -----------------------------------
# 2️⃣ Nested Loop Example
# -----------------------------------

print("\nNested Loop Example:")

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")


# -----------------------------------
# 3️⃣ Multiplication Table Using Nested Loop
# -----------------------------------

print("\nMultiplication Table (1 to 5)")

for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()


# -----------------------------------
# 4️⃣ Simple Pattern Example
# -----------------------------------

print("\nStar Pattern")

rows = 4

for i in range(rows):
    for j in range(i + 1):
        print("*", end=" ")
    print()