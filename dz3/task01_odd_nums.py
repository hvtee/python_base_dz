from random import randint


def create_list(size):
    list_nums = [randint(-50, 50 + 1) for _ in range(size)]
    return list_nums


def find_odd_sum(list1):
    summ = 0
    for num in list1:
        if num % 2 == 1:
            summ += num
    return summ


list_nums = create_list(int(input('Input list size: ')))

print(list_nums)
print(find_odd_sum(list_nums))
