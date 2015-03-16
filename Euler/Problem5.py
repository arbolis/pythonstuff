import itertools
for candidate in itertools.count(232752240):
    if all(candidate % i == 0 for i in range(1, 21)):
        print(candidate)
        break


# This version starts very close to the result I previously got and
# so runs much faster
