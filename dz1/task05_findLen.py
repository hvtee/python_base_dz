import math

coord1 = []
coord2 = []

coord1 = list(map(int, input("Input coord1 (x, y): ").split()))
coord2 = list(map(int, input("Input coord2 (x, y): ").split()))

def findLeng(list1, list2):
    leng = math.sqrt((list1[0] - list2[0]) ** 2 + (list1[1] - list2[1]) ** 2)
    return leng

print(f"Length is: {findLeng(coord1, coord2)}")

########################
# import math

# x1 = int(input("Input x1: "))
# y1 = int(input("Input y1: "))
# x2 = int(input("Input x2: "))
# y2 = int(input("Input y2: "))

# def findLeng(x1, y1, x2, y2):
#      leng = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#      return leng

# print(f"Length is: {findLeng(x1, y1, x2, y2)}")