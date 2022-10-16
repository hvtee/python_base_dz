from math import modf


def create_list_factions(list1: list):
    list_factions = []
    for num in list1:
        list_factions.append(modf(num)[0])
    return list_factions


def find_difference(list1):
    diff = (max(list1)-min(list1))
    print(diff)


list_input = list(map(float, input().split()))
print(list_input)

list_factions = create_list_factions(list_input)
print(list_factions)
find_difference(list_factions)
