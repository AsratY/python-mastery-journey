# 3️⃣ Dictionaries — User Account System

# 🎯 Build: Simple login system.

# 🛠 Use: dictionaries, key access, .get(), .update()

# 📋 Instructions

# Store users as:

# users = {"alice": "1234", "bob": "abcd"}


# Ask for username and password.

# Validate login.

# Allow user registration.

# Prevent duplicate usernames.

# ⭐ Upgrade

# Store login attempts

# Lock account after 3 failures


users = {"alice": "1234", "bob": "abcd"}
attempts = {}
for user in users.keys():
    attempts.update({user: 0})


def user_create():
    new_user_name = input("Create user name: ")
    if new_user_name in users.keys():
        print("User name is already taken!")
        user_create()
    else:
        return new_user_name


while True:
    print("1. Login \n2. Register \n3. List all users \n4. Exit")
    try:
        choise = int(input("Enter your choise: "))
    except:
        print("Enter only 1 , 2 , 3 or 4")
        continue
    if choise == 1:
        user_name = input("Enter your User Name: ")
        pword = input("Enter your password: ")
        if user_name in users.keys():
            if attempts[user_name] == 3:
                print("Account locked due to multiple attempts!!")
            else:
                if pword == users[user_name]:
                    print(f"Welcome {user_name}!")
                    attempts[user_name] = 0
                else:
                    attempts[user_name] = attempts[user_name] + 1
                    print("password incorrect!")
        else:
            print("User doesn't exist!")
    elif choise == 2:
        new_user_name = user_create()
        attempts.update({new_user_name: 0})
        new_pword = input("Create password: ")
        users.update({new_user_name: new_pword})
        print("Registered!")
    elif choise == 3:
        print("Registered users are:")
        counter = 1
        for user in users.keys():
            print(f"\t {counter}. {user}")
            counter += 1
    elif choise == 4:
        break
    else:
        print("Please enter 1 , 2 , 3 or 4")
