# 9️⃣ Exceptions & Errors — Safe Calculator

# 🎯 Build: Crash-proof calculator.

# 🛠 Use: try/except/else/finally

# 📋 Instructions

# Ask for two numbers.

# Ask for operator.

# Handle:

# Division by zero

# Invalid input

# Keep program running until user exits.

# ⭐ Upgrade

# Custom exception messages

# Operation history

from datetime import datetime


class CustomError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def calculator(num_one, num_two, operator):
    match operator:
        case "+":
            return num_one + num_two
        case "-":
            return num_one - num_two
        case "*":
            return num_one * num_two
        case "/":
            return num_one/num_two
        case _:
            raise CustomError("Invalid Operator!!", operator)


operation = dict()

while True:
    try:
        num_one = int(input("Enter first number: "))
        num_two = int(input("Enter second number: "))
    except ValueError as e:
        print(e)
    else:
        operator = input("Enter operator: ")
        try:
            result = calculator(num_one, num_two, operator)
            print(result)
        except CustomError as e:
            print(e.message, e.value)
        except ZeroDivisionError as e:
            print(e)
        else:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            operation.update(
                {time: (num_one, num_two, operator, result)})
            for key, value in operation.items():
                print(
                    f"Time: {key} Operation -> {value[0]} {value[2]} {value[1]} = {value[3]}")
    finally:
        run = input("q to exit, other to continue: ")
    if run == "q":
        break
