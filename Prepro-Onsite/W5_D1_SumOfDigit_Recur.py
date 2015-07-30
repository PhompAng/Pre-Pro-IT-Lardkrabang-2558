""" W5_D1_SumOfDigit_Recur """
def main(inputn, index=0, total=0):
    """ stupid drone """
    if index >= len(inputn) - 1:
        print(total + int(inputn[index]))
        return 0
    main(inputn, index + 1, total + int(inputn[index]))
main(input())
