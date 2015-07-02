""" DaY_Z_Collatz """
def main(inputn):
    """ lnwZa """
    print(int(inputn))
    if inputn != 1:
        if inputn % 2 != 0:
            main((3 * inputn) + 1)
        elif inputn % 2 == 0:
            main(inputn / 2)

main(int(input()))
