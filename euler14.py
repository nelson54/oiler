import math

def callatz_sequence(n, l):
    w = 0
    if n%2 == 0:
        w = n/2
    else:
        w = (3*n+1)/2
    l.append(w)
    return w, l, n

def callatz(next_value):
    arr = []
    while next_value != 1:
        next_value, arr, n = callatz_sequence(next_value, arr)
    return arr

#print(callatz(13))
val = 0
highest = 0
for i in range(1, 1000000):
    #print("Number:", i)
    size = len(callatz(i))
    if highest < size:
        val, highest = i, size
        #print("New Highest:", i)
print("Top:", val)

#print({i: len(callatz(i)) for i in range(15)})
