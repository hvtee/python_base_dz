# def find_sum(some_list):
#     summa = 0
#     for each_number in some_list:
#         digits_sum_list = [int(each_digit) for each_digit in str(each_number)]
#         digits_sum_int = sum(digits_sum_list)
#         if digits_sum_int % 7 == 0:
#             summa += each_number
#         digits_sum_list.clear()
#     return summa
#
#
# required_list = []
# for i in range(1000 + 1):
#     if i % 2 != 0:
#         required_list.append(i ** 3)
#
# print(required_list, sep=' ')
# print(f"Sum is: {find_sum(required_list)}")

############################

def find_sum(numbers_list):
    summa = 0
    for each_number in numbers_list:
        digits_sum = 0
        each_number_copy = each_number
        while each_number_copy != 0:
            digits_sum += each_number_copy % 10
            each_number_copy //= 10
        if digits_sum % 7 == 0:
            summa += each_number
    return summa


def increase_list_number_by17(numbers_list):
    numbers_list = [each_number + 17 for each_number in numbers_list]
    return numbers_list


required_numbers = []
for i in range(1000 + 1):
    if i % 2 != 0:
        required_numbers.append(i ** 3)

print(required_numbers, sep=' ')
print(f"Sum is: {find_sum(required_numbers)}")

required_numbers = increase_list_number_by17(required_numbers)
print(required_numbers, sep=' ')
print(f"Sum is: {find_sum(required_numbers)}")