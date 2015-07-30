""" HW_YO(Yo - Online) - Shield V.1_W3 """
def main():
    """ Minecraft """
    inputn = list(map(int, input().split(" ")))
    print(" " + " _"*(inputn[0]))
    for i in range(inputn[1], 0, -1):
        print(i, end="")
        for j in range(inputn[0]):
            if i == inputn[3] and j == inputn[2] - 1:
                print("|X", end="")
            else:
                print("|_", end="")
        print("|")
    for i in range(inputn[0] + 1):
        print(i, end=" ")
main()
