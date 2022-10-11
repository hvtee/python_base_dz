for x in range(2):
    for y in range(2):
        for z in range(2):
            answer = (not (x or y or z)) == ((not x) and (not y) and (not z))
            print(f"For {x}, {y}, {z} answer is: {answer}")
