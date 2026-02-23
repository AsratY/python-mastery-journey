# 1️⃣ Counter – Log & Analytics System
# 🧾 Exercise: Website Traffic Analyzer

# You are given a list of website visits:

# visits = [
#     "home", "about", "home", "products", "home",
#     "contact", "products", "products", "about",
#     "home", "blog", "blog", "products"
# ]

# ✅ Requirements:

# Count how many times each page was visited.

# Display the 3 most visited pages.

# Find pages visited only once.

# Simulate merging traffic from another server:

# new_visits = ["home", "blog", "blog", "careers"]


# Merge both and show updated counts.

# Remove pages with less than 2 visits.

# 🔥 Real-world relevance:

# Used in analytics dashboards, traffic monitoring, log analysis.


from collections import Counter


def traffic_stats(traffic):
    for page, visited in traffic.items():
        print(f"Page {page} visited {visited} time/s.")

    print()

    top_three_visited = traffic.most_common(3)
    for i, (page, count) in enumerate(top_three_visited, start=1):
        print(f"{i}. {page} is visited {count} times.")

    print()

    for page, visited in traffic.items():
        if visited == 1:
            print(f"Page {page} was visited only once.")

    print()


def traffic_remove(traffic):
    # traffic_cpy = Counter(traffic)
    # for key, value in traffic_cpy.items():
    #     if value < 2:
    #         traffic.pop(key)
    # return traffic
    traffic = Counter(
        # dictionary comprehensions
        {key: count for key, count in traffic.items() if count >= 2})
    return traffic


visits = [
    "home", "about", "home", "products", "home",
    "contact", "products", "products", "about",
    "home", "blog", "blog", "products"
]

traffic = Counter(visits)

traffic_stats(traffic)


new_visits = ["home", "blog", "blog", "careers"]

traffic.update(new_visits)

traffic_stats(traffic)

traffic = traffic_remove(traffic)
traffic_stats(traffic)
