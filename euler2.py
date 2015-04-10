def fibonacci(x, y, m, l):
    n = x + y
    if n > m:
        return l
    else:
        return fibonacci(y, n, m, l+[n])

print(sum([x for x in fibonacci(0, 1, 4000000, [0, 1]) if x % 2 is 0]))