""" W3_D3_Stats """
def fak(mean, mode, median, stdev):
    """ WOWOWOWOWOWOWOWOW """
    if mean % 1 != 0:
        print("Mean = %.4f" % mean)
    else:
        print("Mean = %d" % mean)

    if mode % 1 != 0:
        print("Mode = %.4f" % mode)
    else:
        print("Mode = %d" % mode)

    if median % 1 != 0:
        print("Med = %.4f" % median)
    else:
        print("Med = %d" % median)

    if stdev % 1 != 0:
        print("SD = %.4f" % stdev)
    else:
        print("SD = %d" % stdev)

def main():
    """ World is mine """
    inputn = int(input())
    num = []
    for _ in range(inputn):
        wow = input()
        if "." in wow:
            num.append(float(wow))
        else:
            num.append(int(wow))

    #FIND MEAN
    mean = sum(num) / inputn

    # FIND MODE
    mode = []
    for i in num:
        mode.append(num.count(i))
    if max(mode) > 1:
        mode[0] = num[mode.index(max(mode))]

    #FIND MEDIAN
    if inputn % 2 == 0:
        wow = sorted(num)
        median = float((wow[int(inputn / 2) - 1] + wow[(int(inputn / 2))]) / 2)
    else:
        wow = sorted(num)
        median = (wow[(int((inputn) / 2))])

    #FIND STDEV
    count = 0
    for i in num:
        count += (i - mean)**2
    stdev = (count / (inputn - 1))**0.5

    fak(mean, mode[0], median, stdev)

main()
