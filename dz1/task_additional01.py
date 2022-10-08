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
