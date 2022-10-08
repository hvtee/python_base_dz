day = int(input("Input day of week: "))

if 0 < day < 6:
    print("Its not a day off.")
elif 5 < day < 8:
    print("It a day off.")
else:
    print("Wrong number.")
