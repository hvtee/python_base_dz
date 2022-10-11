# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859»
# будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.


#########################################################

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


required_numbers = []
for i in range(1000 + 1):
    if i % 2 != 0:
        required_numbers.append(i ** 3)

print(required_numbers, sep=' ')
print(f"Sum is: {find_sum(required_numbers)}")

required_numbers = list(map(lambda num: num + 17, required_numbers))

print(required_numbers, sep=' ')
print(f"Sum is: {find_sum(required_numbers)}")
