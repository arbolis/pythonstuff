import itertools
for candidate in itertools.count(12252240):
    if all(candidate % i == 0 for i in range(1, 20)):
        print(candidate)
        break
