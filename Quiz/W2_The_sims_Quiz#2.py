""" W2_The_sims_Quiz#2 """
def main():
    """ WOWWOWO """
    inputn = int(input())
    for line in range(1, inputn + 1):
        print(" "*(inputn - line), end="")
        for _ in range(1, line + 1):
            print("* ", end="")
        print("")
    for line in range(inputn - 1, 0, -1):
        print(" "*(inputn - line), end="")
        for _ in range(1, line + 1):
            print("* ", end="")
        print("")
main()
