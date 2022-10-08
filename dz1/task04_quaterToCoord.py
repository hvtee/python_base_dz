quater = int(input("Input quarter: "))

if quater > 4 or quater < 1:
    print("Wrong quarter.")
    quit()

if quater == 1:
    print("x > 0 and y > 0")
elif quater == 2:
    print("x < 0 and y > 0")
elif quater == 3:
    print("x < 0 and y < 0")
else:
    print("x > 0 and y < 0")
