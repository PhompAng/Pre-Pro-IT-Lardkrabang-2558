""" W2_D2_Pyramid3 """
def main():
    """ WOWOWOWOWOWOWOWWOW """
    inputn = int(input())
    for i in range(1, inputn + 1):
        print(" "*(i - 1), end="")
        print("*"*(((inputn - i) * 2) + 1))
main()
