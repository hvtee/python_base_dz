from random import randint

list1 = [randint(-10, 10) for i in range(10)]
list2 = [randint(-10, 10) for i in range(10)]

list_cross=[]

for i in range(len(list1)):
    if list1[i] in list2 or list1[i] in list_cross:
        list_cross.append(list1[i])

print(list1)
print(list2)
print(list_cross)