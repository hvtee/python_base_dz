from random import randint


def create_polynom(k: int):
    polynom = ''
    for i in range(k, -1, -1):
        coefficient = randint(-10, 10 + 1)
        if coefficient > 0:
            polynom += f'  + {coefficient}x^{i}'
        elif coefficient < 0:
            polynom += f'  - {abs(coefficient)}x^{i}'
    polynom += ' = 0'
    return polynom


def write_polynom(polyn: str, key_: str):
    if key_ != 'a' and key_ != 'w':
        print("Wrong key")
        quit()
    with open('data/polynomials.txt', f'{key_}', encoding='utf-8') as file:
        file.writelines(polyn + '\n')


pow_ = int(input('Input k: '))
key = input('Write/append   w/a?   ')
if pow_ < 0:
    print('Wrong k!')
    quit()

polynom = create_polynom(pow_)
write_polynom(polynom, key)
