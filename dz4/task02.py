def is_prime_factor(number: int):
    list_dividers = [divider for divider in range(1, number // 2 + 1) if number % divider == 0]
    list_dividers.append(number)
    if len(list_dividers) == 2:
        return True
    else:
        return False


def find_prime_factors(num: int):
    list_prime_factors = []
    divider = 2
    while num > 1:
        if is_prime_factor(divider) and num % divider == 0:
            list_prime_factors.append(divider)
            num //= divider
        else:
            divider += 1
    return list_prime_factors


number = int(input('Input number: '))
if number < 1:
    print('Wrong number!')
    quit()

print(find_prime_factors(number))
