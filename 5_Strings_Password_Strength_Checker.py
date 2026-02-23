# 5️⃣ Strings — Password Strength Checker

# 🎯 Build: Password validator.

# 🛠 Use: string methods, loops

# 📋 Instructions

# Ask user to enter a password.

# Check:

# Length ≥ 8

# Contains digit

# Contains uppercase

# Contains special character

# Print why password is weak or strong.

# ⭐ Upgrade

# Mask password output

# Generate password suggestions

import random
import string

upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
number_list = string.digits
special_list = string.punctuation

gen_upper = random.choices(upper_case, k=random.randint(1, 3))
gen_lower = random.choices(lower_case, k=random.randint(5, 7))
gen_number = random.choices(number_list, k=random.randint(1, 3))
gen_special = random.choices(special_list, k=random.randint(1, 3))

pwd_genarated = gen_upper + gen_lower + gen_number + gen_special

random.shuffle(pwd_genarated)

strong_pwd = "".join(pwd_genarated)

pwd = input("Enter password: ")

masked = "*" * len(pwd)

length = len(pwd)
number = 0
upper = 0
special = 0


for letter in pwd:
    if letter.isdigit():
        number += 1
    if letter.isupper():
        upper += 1
    if not letter.isalnum():
        special += 1

if length >= 8 and number > 0 and upper > 0 and special > 0:
    print(
        f"Your password: {masked} is STRONG! Because the characters are {length} with {number} numbers, {upper} upper letter/s and {special} special character/s.")
else:
    print(f"""Your password: {masked} is WEAK! Because:
    length should be equal or above 8 chars yours is {length}
    there should be one or more numbers yours is {number}
    there should be one or more Upper case letters yours is {upper}
    there should be one or more special chars yours is {special}.
    Instead you can use this password {strong_pwd}""")


# more advanced approach for passwords is using secrets
# import secrets
# upper = [secrets.choice(upper_case) for _ in random.ranint(1,3)]
