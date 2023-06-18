import string

password = "dhyanboyisawesome"

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])

lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])

special = any([1 if c in string.punctuation else 0 for c in password])

digits = any([1 if c in string.digits else 0 for c in password])

# c is the variable used to represent each character in the password string. It takes on the value of each character in the password string, one at a time, during each iteration of the list comprehension.

#The above code line is a list comprehension in Python that checks whether each character in a string variable `password` is an uppercase letter or not. Let's break it down:

# 1. `string.ascii_uppercase` is a string constant from the `string` module that contains all the uppercase letters in the ASCII character set ('A' to 'Z').

# 2. The list comprehension iterates over each character `c` in the `password` string.

# 3. For each character `c`, the expression `1 if c in string.ascii_uppercase else 0` is evaluated. This expression checks if `c` is present in the `string.ascii_uppercase`. If it is, it assigns the value 1; otherwise, it assigns the value 0.

# 4. The resulting values (1 or 0) are stored in a list called `upper_case`.

# So, after executing this code line, the `upper_case` list will contain a sequence of 1s and 0s corresponding to whether each character in the `password` string is an uppercase letter or not. The length of the `upper_case` list will be the same as the length of the `password` string. It can be used further for various purposes, such as checking the presence of uppercase letters in a password or performing computations based on the uppercase letters.

characters = [upper_case, lower_case, special, digits]

length = len(password)

score = 0

# In the below code snippet, f is a file object that is created by calling the open() function. 

with open('common.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("Password was found in a common list. Score: 0/7")
    exit()

if length>8:
    score += 1
if length>12:
    score += 1
if length>17:
    score +=1
if length>28:
    score +=1

print(f"Password length is {str(length)}, adding {str(score)} points!")

# An f-string, also known as a formatted string literal, is a way to embed expressions inside string literals by using curly braces

if sum(characters) > 1:
    score +=1

if sum(characters)> 2:
    score += 1

if sum(characters) > 3:
    score +=1

if sum(characters)> 4:
    score += 1

print(f"Password has {str(sum(characters))} different character types, adding {str(sum(characters)-1)} points")

if score<4:
    print(f"The password is quite weak! Score: {str(score)} / 7")

elif score == 4:
    print(f"The password is ok! Score: {str(score)} / 7")

elif 4<score<6:
    print(f"The password is ok! Score: {str(score)} / 7")

elif score>6:
    print(f"The password is strong! Score: {str(score)} / 7")

print(upper_case)

# Learning resources 

# ASCII stands for American Standard Code for Information Interchange. It is a character encoding standard that represents characters using numeric codes. In ASCII, each character is assigned a unique 7-bit code (0 to 127), which can be represented as a decimal, hexadecimal, or binary number.
# For example, the ASCII value for the uppercase letter 'A' is 65, 'B' is 66, and so on. The lowercase letters 'a', 'b', and so on, have ASCII values starting from 97.
# ASCII codes can represent a wide range of characters, including alphabets (uppercase and lowercase), digits (0-9), punctuation marks, special characters, and control characters (such as newline, tab, etc.).

