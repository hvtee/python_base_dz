# def find_digits_sum(num=0):
#     summa = 0
#
#     while num % 10 != 0:
#         num *= 10
#
#     while num > 0:
#         summa += num % 10
#         num = num // 10
#
#     return summa
#
#
# number = float(input("Input number: "))
# print(int(find_digits_sum(number)))

# NOT WORKING
##############################


summa = sum(list(map(int, input("Input number: ").replace('.', '')
                                                 .replace('-', ''))))
print(summa)
