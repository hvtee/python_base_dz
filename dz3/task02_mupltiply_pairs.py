from random import randint


def create_list(size):
    list_nums = [randint(-50, 50 + 1) for _ in range(size)]
    return list_nums


def multiply_pairs(list_old):
    list_new = []
    if len(list_old) % 2 == 0:
        for i in range(len(list_old) // 2):
            list_new.append(list_old[i] * list_old[-(i + 1)])
    if len(list_old) % 2 == 1:
        for i in range(len(list_old) // 2):
            list_new.append(list_old[i] * list_old[-(i + 1)])
        list_new.append(list_old[len(list_old) // 2] ** 2)
    return list_new


list_nums = create_list(int(input('Input list size: ')))

print(list_nums)

list_new = multiply_pairs(list_nums)
print(list_new)
