number = int(input("Input number: "))
list_res = []
for num in range(1, number + 1):
    list_res.append((1 + 1 / num) ** num)

print(sum(list_res).__round__(2))
