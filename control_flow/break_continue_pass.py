"""
LOOP CONTROL STATEMENTS

break
continue
pass

These statements control the behavior of loops.
"""

# -----------------------------------
# 1️⃣ break Statement
# -----------------------------------
# Stops the loop completely

print("Break Example:")

for i in range(1, 10):
    if i == 5:
        break
    print(i)


# -----------------------------------
# 2️⃣ continue Statement
# -----------------------------------
# Skips the current iteration

print("\nContinue Example:")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# -----------------------------------
# 3️⃣ pass Statement
# -----------------------------------
# Placeholder for future code

print("\nPass Example:")

for i in range(3):
    if i == 1:
        pass
    print(i)


# -----------------------------------
# 4️⃣ break in While Loop
# -----------------------------------

print("\nBreak with While Loop:")

count = 1

while True:
    if count == 4:
        break
    print(count)
    count += 1