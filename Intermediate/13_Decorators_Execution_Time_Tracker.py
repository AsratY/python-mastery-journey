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


def performance_analyzer(func):
    def time_checker(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Total Execution Time: {(end - start)*1000}")
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


print(recursion_wrapper(990))


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


print(loop_factorial(990))

# Upgrade will be implimented
