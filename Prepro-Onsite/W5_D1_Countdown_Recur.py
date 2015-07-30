""" W5_D1_Countdown_Recur """
def main(inputn):
    """ wow nee main """
    if inputn < 1:
        print("BOOM!")
        return 0
    print(inputn)
    main(inputn - 1)
main(int(input()))
