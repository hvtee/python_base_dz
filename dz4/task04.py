from random import randint


def create_polynom(k: int):
    polynom = ''
    for i in range(k, -1, -1):
        koefficent = randint(-10, 10 + 1)
        if koefficent > 0:
            polynom += f'  + {koefficent}x{i}'
        elif koefficent < 0:
            polynom += f'  - {abs(koefficent)}x^{i}'
    polynom += ' = 0'
    return polynom


pow_ = int(input('Input k: '))
if pow_ < 0:
    print('Wrong k!')
    quit()

print(create_polynom(pow_))
