# 3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

#############################################

for i in range(1, 100 + 1):
    if i % 10 == 1:
        print(f"{i} процент")
    elif 1 < i % 10 < 5:
        print(f"{i} процента")
    elif 4 < i % 10 < 11 or i % 10 == 0:
        print(f"{i} процентов")