import random


# def make_rnd_list(list_len=10):
#     rnd_list = []
#
#     for x in range(list_len):
#         random_number = random.random()
#         rnd_list.append(random_number)
#     print("\n", "List of elements => ", rnd_list, "\n")
#     return rnd_list


def find_largest_element(list):
    x = 0
    for element in list:
        if element >= x:
            x = element
    return x


def find_largest_elements_from_rnd_list():
    list_len: int = int(input("Let's play, put list length => "))
    make_rnd_list = lambda ll=list_len: [random.randint(0, 100) for x in range(ll)]
    rnd_list: list = make_rnd_list()
    largest_elem = find_largest_element(rnd_list)
    largest_elem_list = []

    for element in rnd_list:
        if element == largest_elem:
            largest_elem_list.append(element)

    print("\n",
          "List of elements = >", rnd_list, "\n",
          "\n",
          f"Largest elements in list = > {len(largest_elem_list)}, and this element => {largest_elem}",
          "\n")
    return largest_elem_list


find_largest_elements_from_rnd_list()
