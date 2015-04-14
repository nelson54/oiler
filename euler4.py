palindromes = []
MIN, MAX = 100, 999


def is_palindrome(p):
    return str(p) == str(p)[::-1]

for x in range(MIN, MAX):
    for n in range(MIN, MAX):
        b = x*n
        if is_palindrome(b):
            palindromes.append(b)

print(max(palindromes))