from math import sqrt
y_new_list = [2, 2]
z_new_list = [1, 1]


for x in range(3, 100):
    for y in range(y_new_list[-1], x):
        if (sqrt(x+y).is_integer() and sqrt(x-y).is_integer()):
            y_new_list.append(x)
            z_new_list.append(y)
            for z in range(z_new_list[-1], y):
                a = x+z
                b = x-z
                c = y+z
                d = y-z
                if (sqrt(a).is_integer() and sqrt(b).is_integer() and
                    sqrt(c).is_integer() and sqrt(d).is_integer()):
                    print("x=", x)
                    print("y=", y)
                    print("z=", z)
                    print("x+y+z=", x+y+z)
print(z_new_list)
print(y_new_list)
