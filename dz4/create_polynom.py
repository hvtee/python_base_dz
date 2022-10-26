from random import randint
import sympy


def create_polynom(k: int):
    polynom_ = ''
    for i in range(k, -1, -1):
        coefficient = randint(-10, 10 + 1)
        if coefficient > 0:
            polynom_ += f'  +{coefficient}*x^{i}'
        elif coefficient < 0:
            polynom_ += f'  -{abs(coefficient)}*x^{i}'
    polynom_ += ' = 0'
    return polynom_


def write_polynom(polyn: str, key_: str):
    if key_ != 'a' and key_ != 'w':
        print("Wrong key")
        quit()
    with open('data/polynomials.txt', f'{key_}', encoding='utf-8') as file:
        file.writelines(polyn + '\n')


def read_polynom():
    polynomials_ = []
    with open('data/polynomials.txt', 'r', encoding='utf-8') as file:
        for line in file:
            polynomials_.append(line)
    return polynomials_


def simplify_polynom(polynomials_):
    for i in range(len(polynomials_)):
        polynomials_[i] = polynomials_[i][:len(polynomials_[i]) - 4]
        polynomials_[i] = polynomials_[i].replace('\n', '')
        polynomials_[i] = polynomials_[i].replace(' ', '')
        polynomials_[i] = sympy.simplify(polynomials_[i])
    return polynomials_


pow_ = int(input('Input k: '))
key = input('Write/append   w/a?   ')
if pow_ < 0:
    print('Wrong k!')
    quit()

polynom = create_polynom(pow_)
write_polynom(polynom, key)


polynomials = read_polynom()
print(simplify_polynom(polynomials))
print(polynomials[0] + polynomials[1])
