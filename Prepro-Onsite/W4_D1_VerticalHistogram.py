""" W4_D1_VerticalHistogram """
def ayano(inputn, char):
    """ Ayano Tateyame """
    num = 0
    for i in range(len(inputn)):
        if inputn[i] == char:
            num += 1
    return num

def letgo(inputn, i, j):
    """ WOW function """
    if i <= ayano(inputn, j):
        print(" *", end="")
    else:
        print("  ", end="")

def main():
    """ Hello, world """
    inputn = input()
    numstring = []
    setstring = sorted(list(set(inputn)))
    for i in setstring:
        numstring.append(ayano(inputn, i))
    setnumstring = list(set(numstring))
    for i in range(max(setnumstring), 0, -1):
        print("%03d" % i, end="")
        for j in setstring:
            if j.islower():
                letgo(inputn, i, j)
        for j in setstring:
            if j.isupper():
                letgo(inputn, i, j)
        print("")
    print("   ", end="")
    for i in setstring:
        if i.islower():
            print(" " + i, end="")
    for i in setstring:
        if i.isupper():
            print(" " + i, end="")
main()
