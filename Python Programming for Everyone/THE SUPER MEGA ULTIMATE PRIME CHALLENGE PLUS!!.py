"""gg ez"""
def primes1(num):
    """ Returns  a list of primes < n """
    if num <= 1:
        return 0
    sieve = [True] * (num//2)
    for i in range(3, int(num**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((num-i*i-1)//(2*i)+1)
    return num//2 - sieve.count(False)

print(primes1(int(input())))
