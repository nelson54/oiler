from itertools import count
print(sum((x for x in count(1) if x <= 10 and not any(i for i in range(2, x) if i % x is 0))))