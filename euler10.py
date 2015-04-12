from itertools import count


print(sum((x for x in range(2000000) if not any(i for i in range(2, x) if x % i is 0))))