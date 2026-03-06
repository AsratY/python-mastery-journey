# 8️⃣ Lambda Functions — Quick Sorting Tool

# 🎯 Build: Sort products by price or rating.

# 🛠 Use: lambda, sorted(key=...)

# 📋 Instructions

# Store products as dictionaries.

# Sort by price.

# Sort by rating.

# Display sorted results.

# ⭐ Upgrade

# Combine multi-field sorting

# User chooses sort criteria


from collections import namedtuple


def print_for_tuple(list_tup):
    for i, item in enumerate(list_tup, start=1):
        print(
            f"{i}. Type: {item.type}  Price: {item.price}  Rating: {item.rating}")
    print()


def print_for_dict(list_dict):
    for i, item in enumerate(list_dict, start=1):
        print(f"{i}.", end=" ")
        for key, value in item.items():
            print(f"{key}: {value}  ", end=" ")
        print()
    print()


Product = namedtuple('Product', 'type,price,rating')

products = [
    Product('laptop', 200, 4.7),
    Product('Mobile', 200, 4.7),
    Product('laptop', 250, 4.9),
    Product('laptop', 1000, 4.8),
    Product('Mobile', 150, 4.5),
    Product('Mobile', 90, 4.4),
    Product('laptop', 1200, 4.8),
    Product('Mobile', 300, 4.6)
]

products_dict = [
    {"Type": "mobile", "Price": 200, "Rating": 4.7},
    {"Type": "laptop", "Price": 250, "Rating": 4.3},
    {"Type": "laptop", "Price": 1200, "Rating": 4.8},
    {"Type": "mobile", "Price": 400, "Rating": 4.4},
    {"Type": "mobile", "Price": 600, "Rating": 4.9},
    {"Type": "laptop", "Price": 700, "Rating": 4.6},
    {"Type": "mobile", "Price": 150, "Rating": 4.2},
    {"Type": "laptop", "Price": 1500, "Rating": 4.9}
]

try:
    user = int(
        input("1. Sort by Rating \n2. Sort by Price \n3. Sort by Rating then Price \n Enter: "))
except ValueError:
    print("Enter Numbers Only!!")
else:
    if user == 1:
        show_rating_tuple = sorted(
            products, key=lambda item: item.rating, reverse=True)
        print("============= USING NAMEDTUPLE ===============")
        print("### Sorted by Rating")
        print_for_tuple(show_rating_tuple)

        show_dict_rating = sorted(
            products_dict, key=lambda item: item["Rating"], reverse=True)
        print("============= USING DICTIONARY ===============")
        print("### Sorted by Rating")
        print_for_dict(show_dict_rating)
    elif user == 2:
        show_price_tuple = sorted(
            products, key=lambda item: item.price, reverse=True)
        print("============= USING NAMEDTUPLE ===============")
        print("### Sorted by Price")
        print_for_tuple(show_price_tuple)

        show_dict_price = sorted(
            products_dict, key=lambda item: item["Price"], reverse=True)
        print("============= USING DICTIONARY ===============")
        print("### Sorted by Price")
        print_for_dict(show_dict_price)
    elif user == 3:
        print("============= SORTED BY RATING THEN PRICE ===============")
        print("####### Using Namedtuple")
        multi_sort_tuple = sorted(
            products, key=lambda item: (item.rating, item.price), reverse=True)
        print_for_tuple(multi_sort_tuple)

        print("####### Using Dictionaries")
        multi_sort_dict = sorted(
            products_dict, key=lambda item: (item["Rating"], item["Price"]), reverse=True)
        print_for_dict(multi_sort_dict)
    else:
        print("WRONG INPUT!!")
