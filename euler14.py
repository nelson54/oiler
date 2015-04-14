import math

def callatz_sequence(n, l):
    w = 0
    if n%2 == 0:
        w = n/2
    else:
        w = 3*n+1
    l.append(w)
    return w, l, n

def callatz(next_value):
    arr = []
    while next_value != 1:
        next_value, arr, n = callatz_sequence(next_value, arr)
    return arr

#print(callatz(13))

print({i: len(callatz(i)) for i in range(25)})
