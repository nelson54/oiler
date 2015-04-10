from math import pow
from itertools import combinations

def isPythagoreanTriplet(a, b, c):
    return a < b < c and pow(a, 2) + pow(b, 2) == pow(c, 2)

print(next(filter(lambda l: l[0] + l[1] + l[2] == 1000 and isPythagoreanTriplet(l[0], l[1], l[2]), combinations(range(1, 1000), 3))))
