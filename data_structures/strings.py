
"""
STRINGS IN PYTHON

A string is a sequence of characters enclosed in quotes.
Strings are immutable in Python.
"""

# -----------------------------------
# 1️⃣ Creating Strings
# -----------------------------------

single_quote = 'Hello'
double_quote = "Python"
multi_line = """This is
a multi-line
string"""

print(single_quote)
print(double_quote)
print(multi_line)


# -----------------------------------
# 2️⃣ String Indexing
# -----------------------------------

text = "Python"

print("First character:", text[0])
print("Last character:", text[-1])


# -----------------------------------
# 3️⃣ String Slicing
# -----------------------------------

word = "Programming"

print(word[0:6])   # Progra
print(word[3:8])   # gramm
print(word[:5])    # Progr
print(word[5:])    # amming


# -----------------------------------
# 4️⃣ String Length
# -----------------------------------

message = "Hello World"

print("Length:", len(message))


# -----------------------------------
# 5️⃣ String Methods
# -----------------------------------

name = "python programming"

print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())


# -----------------------------------
# 6️⃣ Checking String Content
# -----------------------------------

text = "Python123"

print(text.isalpha())
print(text.isdigit())
print(text.isalnum())


# -----------------------------------
# 7️⃣ String Replace
# -----------------------------------

sentence = "I love Java"

new_sentence = sentence.replace("Java", "Python")

print(new_sentence)


# -----------------------------------
# 8️⃣ String Concatenation
# -----------------------------------

first = "Hello"
second = "World"

result = first + " " + second

print(result)


# -----------------------------------
# 9️⃣ f-Strings (Formatted Strings)
# -----------------------------------

name = "Amulya"
age = 20

print(f"My name is {name} and I am {age} years old.")
