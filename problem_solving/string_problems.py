"""
STRING BASED PROBLEMS
"""

# -----------------------
# Problem 1: Reverse a String
# -----------------------

text = "Python"
reverse = text[::-1]
print("Reversed:", reverse)


# -----------------------
# Problem 2: Check Palindrome
# -----------------------

word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# -----------------------
# Problem 3: Count Vowels
# -----------------------

sentence = "I am learning Python"
vowels = "aeiouAEIOU"
count = 0

for char in sentence:
    if char in vowels:
        count += 1

print("Number of vowels:", count)


# -----------------------
# Problem 4: Remove Spaces
# -----------------------

text = "Hello World Python"
print(text.replace(" ", ""))