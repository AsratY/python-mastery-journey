# 🔟 Logging — Application Activity Logger

# 🎯 Build: User activity tracker.

# 🛠 Use: logging module

# 📋 Instructions

# Log:

# Program start

# User actions

# Errors

# Write logs to a file.

# Use different log levels.

# ⭐ Upgrade

# Rotate log files

# Timestamp formatting

import log.activity_logger as activity_logger
import logging

logger = logging.getLogger("activity_logger")
error_logger = logging.getLogger("error_logger")
logger.info("application started")


def divide(num_one, num_two):
    return num_one/num_two


user_name = input("Enter user name: ")

if user_name == "ABC123":
    pwd = input("Enter password: ")
    if pwd == "ABC@123":
        logger.info(f"user {user_name} logged!")
        try:
            num_one = float(input("Enter number one: "))
            num_two = float(input("Enter number two: "))
        except Exception as e:
            error_logger.error(e, extra={"user": user_name})
            logger.info("application stopped by error")
        else:
            try:
                result = divide(num_one, num_two)
            except Exception as e:
                error_logger.error(e, extra={"user": user_name})
                logger.info("application stopped by error")
            else:
                print(f"{num_one} / {num_two} = {result}")
                logger.info("application ended with out error")
    else:
        logger.warning("Incorrect Password!!")
else:
    logger.warning("Incorrect Username!!")
