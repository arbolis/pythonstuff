squares = []
for i in range(1, 2000):
    squares.append(i**2)
for x in range(1, 1000):
    for y in range(1, 1000):
        for z in range(1, 1000):
            a = x+y
            b = x-y
            c = x+z
            d = x-z
            e = y+z
            f = y-z
            if (a in squares and b in squares and c in squares and
                d in squares and e in squares and f in squares):
                print(x)
                print(y)
                print(z)
