""" W5_D1_Armored """
def main():
    """ I already got kongo! """
    dictionary = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    inputn = dictionary.index(input())
    for line in range(1, inputn + 2):
        print(" "*(inputn - line + 1), end="")
        for i in range(line):
            print(dictionary[i], end="")
        for i in range(line - 2, -1, -1):
            print(dictionary[i], end="")
        print("")
    for line in range(inputn, 0, -1):
        print(" "*(inputn - line + 1), end="")
        for i in range(line):
            print(dictionary[i], end="")
        for i in range(line - 2, -1, -1):
            print(dictionary[i], end="")
        print("")
main()
