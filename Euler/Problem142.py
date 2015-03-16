squares = []
for i in range(1, 2000):
    squares.append(i**2)
# Now I choose x>y>z
for x in range(3, 1000):
    for y in range(2, x):
        for z in range(1, y):
            a = x+y
            b = x-y
            c = x+z
            d = x-z
            e = y+z
            f = y-z
            if (a in squares and b in squares and c in squares and
                d in squares and e in squares and f in squares):
                print("x=", x)
                print("y=", y)
                print("z=", z)
                print("x+y+z=", x+y+z)
