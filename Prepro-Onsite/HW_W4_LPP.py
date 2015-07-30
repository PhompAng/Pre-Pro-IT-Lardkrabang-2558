""" HW_W4_LPP """
def ispalindrome(inputn):
    """ Who care? """
    return inputn == inputn[::-1]
def overtwo(inputn):
    """ I don't what i am doing! """
    for i in range(int("9"*inputn), int("9"*inputn) - 101, -1):
        for j in range(i, i - (10 ** (inputn - 1)) + 2, -1):
            if ispalindrome(str(i * j)):
                print(i * j)
                return 0
def minorequaltwo(inputn):
    """ This function use docstring from above function """
    for i in range(int("9"*inputn), 0, -1):
        for j in range(i, 0, -1):
            if ispalindrome(str(i * j)):
                print(i * j)
                return 0
def main():
    """ Who care? """
    inputn = int(input())
    if inputn > 2:
        overtwo(inputn)
    else:
        minorequaltwo(inputn)
main()
