""" DaY_Z_Almstmin """
def main(inputn):
    """ xsdfj;;jfg """
    if inputn == 0:
        print("NONE")
    else:
        number = []
        for i in range(inputn):
            number.append(int(input()))
        number.sort()
        for i in range(inputn - 1):
            if number[i] != number[i + 1]:
                print(number[i + 1])
                return 0
        print("NONE")
main(int(input()))
