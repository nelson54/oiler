from itertools import count
from functools import reduce
from operator import mul


def primeFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def numberOfDivisors(n):
    exponents = {}
    for a in primeFactors(n):
        if a in exponents:
            exponents[a] += 1
        else:
            exponents[a] = 1

    return reduce(mul, map(lambda x: x+1, exponents.values()))

print(next(sum(range(n)) for n in count(1) if n > 2 and numberOfDivisors(sum(range(n))) > 500))