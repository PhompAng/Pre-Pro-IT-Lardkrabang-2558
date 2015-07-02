""" MEGA PRIME """
def trans(n):
    "hello"
    return n * 2 + 3
def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1)) # leave off `list()` in Python 2
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): # use `xrange()` in Python 2
        if s[i]:
            # next line:  use `xrange()` in Python 2
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)

def main(limit):
    if limit < 2:
        print("0")
    else:
        count = 0
        for i in sieve(limit):
            print(i, "is a prime number.")

main(int(input()))
