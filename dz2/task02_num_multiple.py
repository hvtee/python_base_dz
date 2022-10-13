number = int(input("Input number: "))
res = 1
for numb in range(1, number + 1):
    res = res * numb
    print(*range(1, numb + 1), sep=' * ')
