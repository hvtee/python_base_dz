import math

coord1 = list(map(int, input("Input coord1 (x, y): ").split()))
coord2 = list(map(int, input("Input coord2 (x, y): ").split()))


def find_length(list1, list2):
    length = math.sqrt((list1[0] - list2[0]) ** 2 + (list1[1] - list2[1]) ** 2)
    return length


print(f"Length is: {find_length(coord1, coord2)}")