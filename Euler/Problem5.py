import itertools
for candidate in itertools.count(11):
    if all(candidate % i == 0 for i in range(1, 21)):
        print(candidate)
        break
