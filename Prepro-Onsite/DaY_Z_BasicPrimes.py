""" DaY_Z_BasicPrimes """
def trans(inputn):
    "hello"
    return inputn * 2 + 3
def sieve(inputn):
    "Return all primes <= n."
    np1 = inputn + 1
    inputs = list(range(np1)) # leave off `list()` in Python 2
    inputs[1] = 0
    sqrtn = int(round(inputn**0.5))
    for i in range(2, sqrtn + 1): # use `xrange()` in Python 2
        if inputs[i]:
            # next line:  use `xrange()` in Python 2
            inputs[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, inputs)

def main(limit):
    """ MUTSU IS WAIFU !! """
    if limit < 2:
        print("")
    else:
        for i in sieve(limit):
            print(i, "is a prime number.")

main(int(input()))
