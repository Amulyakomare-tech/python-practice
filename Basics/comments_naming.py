"""
COMMENTS AND NAMING CONVENTIONS IN PYTHON
"""

# -------------------------
# 🔹 1. COMMENTS
# -------------------------

# Single line comment

"""
Multi-line comment
Used for explanation or documentation
"""

# Example:

name = "Amulya"  # storing user name
age = 20  # storing age


# -------------------------
# 🔹 2. WHY COMMENTS?
# -------------------------

# - Improves readability
# - Helps other developers understand logic
# - Important in teamwork


# -------------------------
# 🔹 3. NAMING CONVENTIONS
# -------------------------

# Python follows PEP 8 style guide.

# ✅ Variables → snake_case
student_name = "Rahul"
total_marks = 450

# ❌ Avoid this:
# StudentName
# totalMarks


# -------------------------
# 🔹 4. CONSTANTS
# -------------------------

# Constants are written in CAPITAL LETTERS

PI = 3.14159
MAX_LIMIT = 100


# -------------------------
# 🔹 5. FUNCTION NAMING
# -------------------------

def calculate_total(a, b):
    return a + b


print(calculate_total(10, 20))


# -------------------------
# 🔹 PRACTICE
# -------------------------

# Rename badly written variables properly

A = 10
B = 20

sum_result = A + B
print(sum_result)