"""
PATTERN PROBLEMS - DAY 1
Focus: Nested Loops Understanding
"""

# -----------------------------------
# Pattern 1: Solid Square
# -----------------------------------
# Expected Output:
# * * * *
# * * * *
# * * * *
# * * * *

print("Pattern 1: Solid Square")

rows = 4

for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()

print("\n")  # spacing


# -----------------------------------
# Pattern 2: Right Triangle
# -----------------------------------
# *
# * *
# * * *
# * * * *

print("Pattern 2: Right Triangle")

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n")


# -----------------------------------
# Pattern 3: Reverse Triangle
# -----------------------------------

print("Pattern 3: Reverse Triangle")

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
