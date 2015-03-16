from math import sqrt

for x in range(3, 1000):
    for y in range(2, x):
        for z in range(1, y):
            a = x+y
            b = x-y
            c = x+z
            d = x-z
            e = y+z
            f = y-z
            if (type(sqrt(a)) == int and type(sqrt(b)) == int and
                type(sqrt(c)) == int and type(sqrt(d)) == int and
                type(sqrt(e)) == int and type(sqrt(f)) == int):
                print("x=", x)
                print("y=", y)
                print("z=", z)
                print("x+y+z=", x+y+z)
