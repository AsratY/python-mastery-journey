# 1️⃣3️⃣ Decorators — Execution Time Tracker

# 🎯 Build: Performance analyzer.

# 🛠 Use: decorators

# 📋 Instructions

# Create a decorator that measures execution time.

# Apply it to slow functions.

# Print timing output.

# ⭐ Upgrade

# Log performance data

# Count function calls

import time
import logging


logger = logging.getLogger(__name__)
file_h = logging.FileHandler('./log/performance.log')
file_h.setLevel(logging.DEBUG)
file_f = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(name)s - %(function)s - %(message)s', '%Y-%b-%d-%a %H:%M:%S')
file_h.setFormatter(file_f)
logger.addHandler(file_h)
logger.setLevel(logging.DEBUG)


def performance_analyzer(func):
    counter = 0

    def time_checker(*args, **kwargs):
        nonlocal counter
        counter += 1
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        performance = (end - start)*1000
        logger.debug(f"Total Execution Time: {performance}",
                     extra={"function": func.__name__})
        print(
            f"Total Execution Time: {performance} \nFunction: {func.__name__} called {counter} Times")
        return result
    return time_checker

# using closure to hide recursion from decorator


@performance_analyzer
def recursion_wrapper(value):
    def recursion_factorial(number):
        if number == 1:
            return 1
        else:
            return number * recursion_factorial(number-1)
    return recursion_factorial(value)


@performance_analyzer
def loop_factorial(number):
    i = number
    j = number-1
    value = 1
    while i >= 1:
        if j <= 1:
            value = value * i
            break
        value = value * i*j

        j -= 2
        i -= 2

    return value


recursion_wrapper(990)
loop_factorial(990)
recursion_wrapper(990)
loop_factorial(990)
recursion_wrapper(990)
loop_factorial(990)
recursion_wrapper(990)
loop_factorial(990)
recursion_wrapper(990)
loop_factorial(990)
