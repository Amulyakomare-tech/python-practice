"""
LOOPS IN PYTHON
Used to repeat a block of code multiple times.
"""

# -----------------------------------
# 1️⃣ For Loop
# -----------------------------------

print("For Loop Example:")

for i in range(1, 6):
    print(i)


# -----------------------------------
# 2️⃣ While Loop
# -----------------------------------

print("\nWhile Loop Example:")

count = 1

while count <= 5:
    print(count)
    count += 1


# -----------------------------------
# 3️⃣ Looping Through a String
# -----------------------------------

print("\nLoop Through String:")

text = "Python"

for char in text:
    print(char)


# -----------------------------------
# 4️⃣ Looping Through a List
# -----------------------------------

print("\nLoop Through List:")

numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)


# -----------------------------------
# 5️⃣ Nested Loops
# -----------------------------------

print("\nNested Loop Example:")

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")


# -----------------------------------
# 6️⃣ Using break and continue
# -----------------------------------

print("\nBreak Example:")

for i in range(1, 6):
    if i == 4:
        break
    print(i)

print("\nContinue Example:")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)