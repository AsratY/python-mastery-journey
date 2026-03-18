# 1️⃣1️⃣ JSON — User Data Storage App

# 🎯 Build: Persistent user system.

# 🛠 Use: json.load, json.dump

# 📋 Instructions

# Save users to a JSON file.

# Load users at startup.

# Add, delete, update users.

# Auto-save changes.

# ⭐ Upgrade

# Encrypt passwords

# Backup file system

import json
import base64
from cryptography.fernet import Fernet
from getpass import getpass
import shutil
import os

keys = Fernet.generate_key()
cipher = Fernet(keys)


class CustomError(Exception):
    def __init__(self, message, value):
        super().__init__(message)
        self.message = message
        self.value = value


def save_to_file(users):
    base_file = './data/users.json'
    backup_file = './data/users_backup.json'
    if os.path.exists(base_file):
        shutil.copy(base_file, backup_file)
    with open('./data/users.json', "w") as data:
        json.dump(users, data, indent=4)


def load_from_file():
    with open('./data/users.json', 'r') as data:
        try:
            return json.load(data)
        except json.decoder.JSONDecodeError:
            with open('./data/users_backup.json', 'r') as backup_data:
                try:
                    print("I ended up here")
                    return json.load(backup_data)
                except json.decoder.JSONDecodeError:
                    users = {
                        "users": [
                            {
                                "name": ''
                            }
                        ]
                    }
                    return users


def check_age(age):
    if age < 18:
        raise CustomError("Under Age!!", age)


users = {
    "users": [
        {
            "name": "Jhon",
            "password": '',
            "age": 30,
            "city": "New York",
            "hasChildren": False,
            "titles": ["engineer", "programmer"],
            "key": ''
        },
        {
            "name": "Dave",
            "password": '',
            "age": 32,
            "city": "DC",
            "hasChildren": False,
            "titles": ["artist", "programmer"],
            "key": ''
        }
    ]
}


users_dict = dict()
# users_dict = users.copy()
while True:
    try:
        if not users_dict:
            users_dict = load_from_file()
    except FileNotFoundError:
        print("Error Loading from file!")
        break
    else:
        if users_dict:
            print("======== USERS ========")
            for i, user in enumerate(users_dict["users"], start=1):
                print(f"{i}. {user['name']}")
            print("=======================")
    try:
        action = int(
            input("1. Add User \n2. Delete User \n3. Update User \n4. Login Check \n5. Exit \n => "))
    except ValueError:
        print("Please only numbers!!")
    else:
        if action == 1:
            name = input("Enter name: ")
            pwd = getpass("Enter password: ")
            pwd = pwd.encode('utf-8')
            pwd = cipher.encrypt(pwd)
            pwd = base64.b64encode(pwd).decode('utf-8')
            try:
                age = int(input("Enter age: "))
                check_age(age)
            except ValueError:
                print("please only enter numbers!!")
            except CustomError as e:
                print(e.message, e.value)
            else:
                city = input("Enter city: ")
                children = input("Do you have children(y/n): ")
                if children.lower() == "y" or children.lower() == 'yes':
                    children = True
                else:
                    children = False
                profession = input("Enter your profession/s: ")

                users_dict["users"].append(
                    {
                        "name": name,
                        "password": pwd,
                        "age": age,
                        "city": city,
                        "hasChildren": children,
                        "titles": list(profession.strip().split(" ")),
                        "key": base64.b64encode(keys).decode('utf-8')
                    })
                save_to_file(users_dict)
        elif action == 2:
            name = input("Enter name: ")
            users_dict["users"] = [
                user for user in users_dict["users"] if user["name"] != name
            ]
            save_to_file(users_dict)
            continue
        elif action == 3:
            name = input("Enter name of the user to update: ")
            user = next(
                (user for user in users_dict["users"] if user["name"] == name), None)
            if not user:
                print("User Doesn't Exist!!!")
            else:
                print("\n=====   Current Values   =====")
                for key, value in user.items():
                    print(f"{key} : {value}")
                print("==============================")
                field = input("Which data you want to update? ")
                if field in user.keys():
                    if field == "age":
                        try:
                            age = int(input("Enter value: "))
                            check_age(age)
                        except ValueError:
                            print("Please enter numbers only!")
                            continue
                        except CustomError as e:
                            print(e.message, e.value)
                        else:
                            user[field] = age
                    elif field == "password":
                        pwd = getpass("Enter new password: ")
                        pwd = pwd.encode('utf-8')
                        encrypted = cipher.encrypt(pwd)
                        encrypted = base64.b64encode(encrypted).decode('utf-8')
                        user[field] = encrypted
                        user["key"] = base64.b64encode(keys).decode('utf-8')
                    elif field == "titles":
                        values = input("Enter titles: ")
                        user[field] = values.strip().split(" ")
                    elif field == "hasChildren":
                        value = input("Does he/she has children? (y/n)")
                        if value.lower() == "y" or value.lower() == 'yes':
                            user[field] = True
                        else:
                            user[field] = False
                    else:
                        user[field] = input("Enter value: ")
                else:
                    print("Data doesn't exist!!!!")
            save_to_file(users_dict)

        elif action == 4:
            name = input("enter user name: ")
            user = next((user for user in users_dict["users"]
                        if user["name"] == name), None)
            if user:
                pwd = getpass("enter password: ")
                pwd_str = base64.b64decode(user["password"])
                key = base64.b64decode(user["key"])
                cipher_stored = Fernet(key)
                pwd_str = cipher_stored.decrypt(pwd_str)
                pwd_str = pwd_str.rstrip(b"\0").decode('utf-8')
                if pwd_str == pwd:
                    print("Logged In!!")
                else:
                    print("Incorrect Password!!")
            else:
                print("User Doesn't Exist!!!")
        elif action == 5:
            break
        else:
            print("Only choose from the menu above!!")
