# 4️⃣ Sets — Unique Visitor Tracker

# 🎯 Build: Track unique website visitors.

# 🛠 Use: sets, add/remove, intersection

# 📋 Instructions

# Simulate daily visitors using lists.

# Convert lists to sets.

# Show:

# Total unique visitors

# Returning visitors

# New visitors

# ⭐ Upgrade

# Compare visitors across 3 days

# Show loyal visitors (visited every day)


monday_list = ["alice", "bob", "charlie", "alice", "david", "emma", "bob"]
tuesday_list = ["bob", "emma", "frank", "george", "bob", "harry", "alice"]
wednesday_list = ["bob", "emma", "frank", "marry", "bob", "harry", "alice"]

day_one = set(monday_list)
day_two = set(tuesday_list)
day_three = set(wednesday_list)

print(f"Total Unique Visitors are: {set.union(day_one, day_two, day_three)}")
print(
    f"This visitors Returned on Tuesday: {set.intersection(day_one, day_two)} and this visitors returned on Wedensday: {set.intersection((set.union(day_one, day_two)), day_three)}")
print(
    f"New vistors on Tuesday:{set.difference(day_two, day_one)} and new visitors on wednesday: {set.difference(day_three, (set.union(day_one, day_two)))}")
print(f"Loyal Visitors are: {set.intersection(day_one, day_two, day_three)}")
