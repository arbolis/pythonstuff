import itertools
# I start with candidate=20 and I increement by steps of 20. Nice trick
# and no hack, that is, the seed is 20 and not close to the solution.
for candidate in itertools.count(20, 20):
    if all(candidate % i == 0 for i in range(1, 21)):
        print(candidate)
        break


# This version starts very close to the result I previously got and
# so runs much faster
