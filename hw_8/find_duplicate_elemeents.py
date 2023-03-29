import random


def find_duplicate_elements_from_rwo_lists(lst1, lst2):
    set1 = set(lst1)
    print(f"set1 -> {set1}")
    set2 = set(lst2)
    print(f"set2 -> {set2}")
    duplicate_elements = set1.intersection(set2)
    return print(f"Duplicate elements -> {duplicate_elements}")


rnd_lst1 = random.sample(range(1, 30), 9)
print(f"rnd_lst1 -> {rnd_lst1}")
rnd_lst2 = random.sample(range(1, 30), 15)
print(f"rnd_lst2 -> {rnd_lst2}")


find_duplicate_elements_from_rwo_lists(rnd_lst1, rnd_lst2)
