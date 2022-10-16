from random import randint


def create_list(num):
    list_res = []
    if num == 0:
        return list_res
    list_res = [randint(-number, number) for i in range(number)]
    return list_res


def fill_file(num):
    with open('file.txt', 'w', encoding='utf-8') as file:
        for i in range(num // 2):
            file.write(str(randint(-num, num)) + '\n')


def read_file():
    # data = []
    # with open("file.txt", 'r', encoding='utf-8') as file:
    #     for line in file:
    #         data.append([int(x) for x in line.split()])
    with open("file.txt", 'r', encoding='utf-8') as file:
        file = file.read().splitlines()
    return file


def multiple(list_nums, list_pos):
    if len(list_nums) == 0:
        return 0
    res = 1
    for i in range(len(list_pos)):
        res *= list_nums[int(list_pos[i])]
    return res


number = abs(int(input("Input number: ")))

list1 = create_list(number)
print(list1, sep=' ')

fill_file(number)
list_from = read_file()
list_from = list(map(int, list_from))
print(list_from)

print(multiple(list1, list_from))
