from itertools import count, islice
next(islice((x for x in count(1) if not any(i for i in range(2, x) if x % i is 0)), 10001, None), None)