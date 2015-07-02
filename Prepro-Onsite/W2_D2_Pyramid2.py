""" W2_D2_Pyramid2 """
def main():
    """ WOWOWOWOWOWOWOWWOW """
    inputn = int(input())
    count = 1
    for i in range(inputn):
        for j in range(inputn - (i + 1)):
            print(" "*(j - j + 1), end="")
        for j in range(count):
            print("*", end="")
        count += 2
        print("")
main()
