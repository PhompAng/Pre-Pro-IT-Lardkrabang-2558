""" W4_D1_HorizontalHistogram """
def c0unt(inputn, char):
    """ WOW c0unt """
    num = 0
    for i in range(len(inputn)):
        if inputn[i] == char:
            num += 1
    return num

def kongo(inputn, char):
    """ This is a DocString """
    for j in range(c0unt(inputn, char)):
        if j % 5 == 0 and j != 0:
            print("|", end="")
        print("-", end="")
    print("")

def main():
    """ WOW Minecraft """
    inputn = input()
    setstring = sorted(list(set(inputn)))
    for i in range(len(setstring)):
        if setstring[i].islower():
            print(setstring[i] + " : ", end="")
            kongo(inputn, setstring[i])
    for i in range(len(setstring)):
        if setstring[i].isupper():
            print(setstring[i] + " : ", end="")
            kongo(inputn, setstring[i])
main()
