def covert_10_to_2(number_10):
    number_2 = []
    while number_10 != 0:
        number_2.append(number_10 % 2)
        number_10 //= 2
    number_2.reverse()
    return number_2


num_in_10 = int(input('Input number: '))
num_in_2 = []
num_in_2 = covert_10_to_2(num_in_10)
print(num_in_2)
