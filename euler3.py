def factors(n):
    return [f for f in range(1, n) if n % f is 0 and any(num % a == 0 for a in range(2, num))]

print([x for x in factors(13195) if 2 % x is 0])