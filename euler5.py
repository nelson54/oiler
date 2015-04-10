from fractions import gcd
from functools import reduce

def lcm(numbers):
    return reduce(lambda x, y: (x*y)/gcd(x, y), numbers, 1)

print(lcm(range(1, 20)))
