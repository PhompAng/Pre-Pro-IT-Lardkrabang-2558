""" W4_Perfect#Quiz4 """
def main():
    """ WOW awesome """
    inputn = int(input())
    sumofsum, perfect = 0, list()
    for _ in range(1, 100, 2):
        if _ == 1:
            perfect.append((2**_) * (2**(_ + 1) - 1))
        else:
            perfect.append((2**(_ - 1)) * (2**_ - 1))
    for i in range(1, inputn + 1):
        if i in perfect:
            sumofsum += i
    print(sumofsum)
main()
