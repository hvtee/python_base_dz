x = int(input("Input x: "))
y = int(input("Input y: "))

if x == 0 or y == 0:
    print("Not 0")
    quit()

if x > 0 and y > 0:
    print("Quarter I")
elif x < 0 and y > 0:
    print("Quarter II")
elif x < 0 and y < 0:
    print("Quarter III")
else:
    print("Quarter IV")
