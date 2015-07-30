""" W5_D1_Factorial_Recur """
def main(inputn):
    """ wow recursive """
    if inputn > 1:
        return inputn * main(inputn - 1)
    return 1
print(main(int(input())))
