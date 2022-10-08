### 1. Реализовать вывод информации о промежутке времени в зависимости от
# его продолжительности duration в секундах: до минуты:
# <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:
#
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

##########################################################

# time = int(input("Input time in seconds: "))
time_list = [53, 153, 4153, 400153]

seconds = minutes = hours = days = 0

for time in time_list:
    if time < -1:
        print("Wrong time")
        quit()

    if time < 60:
        seconds = time
        print(f"{seconds}s")
    elif time < 3600:
        minutes = time // 60
        seconds = time % 60
        print(f"{minutes}m {seconds}s")
    elif time < 86400:
        hours = time // 3600
        minutes = time % 3600 // 60
        seconds = time % 3600 % 60
        print(f"{hours}h {minutes}m {seconds}s")
    else:
        days = time // 86400
        hours = time % 86400 // 3600
        minutes = time % 86400 % 3600 // 60
        seconds = time % 86400 % 3600 % 60
        print(f"{days}d {hours}h {minutes}m {seconds}s")
