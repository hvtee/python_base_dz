def find_number_accuracy(numb: float, d: str):
    return round(numb, len(d.split('.')[1]))


accuracy = input('Input accuracy d: ')
number = float(input('Input number: '))

if float(accuracy) > 1:
    print('Wrong accuracy!')
    quit()

print(find_number_accuracy(number, accuracy))
