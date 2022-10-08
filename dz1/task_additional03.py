for i in range(1, 100 + 1):
    if i % 10 == 1:
        print(f"{i} процент")
    elif 1 < i % 10 < 5:
        print(f"{i} процента")
    elif 4 < i % 10 < 11 or i % 10 == 0:
        print(f"{i} процентов")
