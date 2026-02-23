# 2️⃣ Tuples — Configuration Manager

# 🎯 Build: A read-only app configuration system.

# 🛠 Use: tuples, unpacking, immutability

# 📋 Instructions

# Create a tuple like:

# config = ("localhost", 5432, "admin", True)


# Unpack the tuple into variables.

# Print configuration in a formatted way.

# Try (and fail) to modify the tuple—handle the error gracefully.

# ⭐ Upgrade

# Store multiple configurations in a list of tuples

# Select a config by index

config = ("localhost", 5432, "admin", True)
host, port, user, debug_mode = config

print(
    f"The host is {host}, the port is {port}, the user is {user} and the Debug Mode is {debug_mode}.")

try:
    config[0] = "digital_ocean"
except:
    print("Can not assign new value to a Tuple!\n")

config_list = [("Google Clouds", 5432, "admin", True), ("Digital Ocean",
                                                        80, "admin", False), ("AWS", 4020, "user001", False)]

for item in config_list:
    print(
        f"The host is {item[0]}, the port is {item[1]}, the user is {item[2]} and the Debug Mode is {item[3]}.")
