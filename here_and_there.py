# ======Learning Topics=======

# list comprehension
# dict comprehension
# set and generator comprehensions
sample_list = [11, 12, 3, 4, 4, 5, 45, 45, 45, 6, 23, 43, 7, 456, 7]

list_sum = sum(number for number in sample_list)
print(list_sum)


list_filter = [number + 5 if number ==
               45 else number for number in sample_list if number > 5]
list_sum = sum(number for number in list_filter)
print(list_sum)
