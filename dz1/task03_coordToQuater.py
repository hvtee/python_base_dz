x = int(input("Input x: "))
y = int(input("Input y: "))

if x == 0 or y == 0:
    print("Not 0")
    quit()

if x > 0 and y > 0:
    print("Quater I")
elif x < 0 and y > 0:
    print("Quater II")
elif x < 0 and y < 0:
    print("Quater III")
else:
    print("Quater IV")
