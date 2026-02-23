# 3️⃣ OrderedDict– LRU Cache Simulation
# ️ Exercise: Build a Simple LRU Cache
# Create a cache system with capacity = 3.
# ️ Requirements:
# 1. Add key-value pairs (like page caching):
# 2. cache.put("home", "HTML data")
# 3. When capacity exceeds 3:
#   o Remove the least recently used item.
# 4. When accessing an item:
#   o Move it to the end (most recently used).
# 5. Print cache state after each operation.
# ️ Real-world relevance:
# Browser caching, API caching, database query caching.

from collections import OrderedDict

CAPACITY = 3


def capacity_limit(cache):
    if len(cache) > CAPACITY:
        cache.popitem(last=False)
    return cache


def access_cache(cache, cache_key):
    if cache_key in cache:
        print(f"{cache_key} : {cache[cache_key]}")
        cache.move_to_end(cache_key)
    return cache


def add_cache(cache, key, value):
    if key in cache:
        cache.update({key: value})
        cache.move_to_end(key)
    else:
        cache.update({key: value})
        cache = capacity_limit(cache)
    return cache


cache = OrderedDict()
cache["home"] = "5"
cache["live"] = "4"
cache["about"] = "2"
cache["home_2"] = "2"

cache = capacity_limit(cache)


cache = access_cache(cache, "live")

while True:
    for i, (key, value) in enumerate(cache.items(), start=1):
        print(f"{i}. {key.capitalize()}")
    print("4. Add Cache")
    print("5. Exit")
    try:
        choice = int(input("Enter: "))
        if choice == 1:
            key = list(cache.keys())[0]
            cache = access_cache(cache, key)
            continue
        elif choice == 2:
            key = list(cache.keys())[1]
            cache = access_cache(cache, key)
            continue
        elif choice == 3:
            key = list(cache.keys())[2]
            cache = access_cache(cache, key)
            continue
        elif choice == 4:
            key = input("Enter Page: ")
            if key in cache.keys():
                print("The Page already exists!")
                value = input("Enter Data: ")
                cache = add_cache(cache, key, value)
            else:
                value = input("Enter Data: ")
                cache = add_cache(cache, key, value)
            continue
        elif choice == 5:
            break
        else:
            print("Enter only from the above listed!")
            continue
    except ValueError:
        print("Enter only from the choice!")
        continue
