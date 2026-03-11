"""
DICTIONARIES IN PYTHON

A dictionary stores data in key-value pairs.
Keys must be unique and immutable.
"""

# -----------------------------------
# 1️⃣ Creating a Dictionary
# -----------------------------------

student = {
    "name": "Amulya",
    "age": 20,
    "course": "BCA"
}

print(student)


# -----------------------------------
# 2️⃣ Accessing Values
# -----------------------------------

print(student["name"])
print(student.get("age"))


# -----------------------------------
# 3️⃣ Adding or Updating Values
# -----------------------------------

student["age"] = 21
student["city"] = "Hyderabad"

print(student)


# -----------------------------------
# 4️⃣ Removing Items
# -----------------------------------

student.pop("city")

print(student)


# -----------------------------------
# 5️⃣ Dictionary Keys, Values, Items
# -----------------------------------

print(student.keys())
print(student.values())
print(student.items())


# -----------------------------------
# 6️⃣ Looping Through Dictionary
# -----------------------------------

for key, value in student.items():
    print(key, ":", value)