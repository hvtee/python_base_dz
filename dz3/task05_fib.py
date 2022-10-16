def fibonachhi(num: int):
    fib = [1, 0, 1]
    for i in range(3, num + 2):
        fib.append(fib[i - 1] + fib[i - 2])
    for i, j in zip(range(2, num + 2), range(2, num+num, 2)):
        fib.insert(0, (-1)**(i+1)*fib[j+1])
    return fib


num = int(input('Input number: '))
fib = fibonachhi(num)
print(fib)
