""" W5_D1_Countup_Recur """
def main(inputn, index=1):
    """ wow nee main """
    if index <= inputn:
        print(index)
        main(inputn, index + 1)
    else:
        return 0
main(int(input()))
