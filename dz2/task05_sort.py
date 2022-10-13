from random import randint
from random import shuffle

number = int(input('Input list size: '))

list1 = [randint(-50, 50) for i in range(number)]
print(list1)

shuffle(list1)
print(list1)
