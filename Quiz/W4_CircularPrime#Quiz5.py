""" W4_CircularPrime#Quiz5 """
import math
def isprime(inputn):
    """ WOW This is a Prime ? """
    if inputn == 2:
        return True
    if inputn <= 1:
        return False
    for i in range(2, math.ceil((inputn)**0.5) + 1):
        if inputn % i == 0:
            return False
    return True
def main():
    """ WOW This is a main ? """
    inputn = input()
    getsum = 0
    for char in range(2, int(inputn) + 1):
        count = 0
        for _ in range(len(str(char))):
            char = str(char)[1:] + str(char)[0]
            if isprime(int(char)):
                count += 1
        if count == len(str(char)):
            getsum += int(char)
    print(getsum)
main()
