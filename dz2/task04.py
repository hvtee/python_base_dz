from random import randint


def create_list(num):
    list_res = []
    if num == 0:
        return list_res
    list_step = [randint(-number + 1, number - 1) for i in range(number - 2)]
    list_res = [-number, *list_step, number]
    return list_res


def fill_file(num):
    with open('file.txt', 'w', encoding='utf-8') as file:
        for i in range(num // 2):
            file.write(str(randint(-num, num)) + '\n')


def read_file():
    data = []
    with open("file.txt") as file:
        for line in file:
            data.append([int(x) for x in line.split()])
    return data


def multiple(list_nums, list_pos):
    if len(list_nums) == 0:
        return 0
    res = 1
    for i in range(len(list_pos)):
        res *= list_nums[int(list_pos[i][0])]
    return res


number = abs(int(input("Input number: ")))

list1 = create_list(number)
print(list1, sep=' ')

fill_file(number)
list_from = read_file()
print(list_from)

print(multiple(list1, list_from))
