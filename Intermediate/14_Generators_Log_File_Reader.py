# 1️⃣4️⃣ Generators — Log File Reader

# 🎯 Build: Efficient file reader.

# 🛠 Use: yield

# 📋 Instructions

# Read a large file line by line.

# Yield one line at a time.

# Filter lines with errors.

# ⭐ Upgrade

# Yield only specific log levels

# Count occurrences


def file_read(log_level):
    with open('./log/generators.log', 'r') as log:
        for line in log:
            if log_level:
                if log_level in line:
                    yield line
            else:
                yield line


try:
    log_level = int(input(
        "1. ERROR \n2. INFO \n3. DEBUG \n4. INFO and DEBUG \n5. ALL \n => "))
except ValueError:
    print("Only Numbers!!")
else:
    error_count = 0
    debug_count = 0
    info_count = 0
    if log_level == 1:
        for log_line in file_read("- ERROR -"):
            print(log_line, end="")
            error_count += 1
        print(f"ERROR: {error_count}")
    elif log_level == 2:
        for log_line in file_read("- INFO -"):
            print(log_line, end="")
            info_count += 1
        print(f"INFO: {info_count}")
    elif log_level == 3:
        for log_line in file_read("- DEBUG -"):
            print(log_line, end="")
            debug_count += 1
        print(f"DEBUG: {debug_count}")
    elif log_level == 4:
        for log_line in file_read(""):
            if "- DEBUG -" in log_line:
                debug_count += 1
                print(log_line, end="")
            elif "- INFO -" in log_line:
                info_count += 1
                print(log_line, end="")
        print(f"DEBUG: {debug_count}")
        print(f"INFO: {info_count}")
    elif log_level == 5:
        for log_line in file_read(""):
            print(log_line, end="")
            if "- ERROR -" in log_line:
                error_count += 1
            elif "- INFO -" in log_line:
                info_count += 1
            elif "- DEBUG -" in log_line:
                debug_count += 1
        print(
            f"ERROR: {error_count}\nDEBUG: {debug_count}\nINFO: {info_count}")
    else:
        print("Only Enter from the choise!!")
