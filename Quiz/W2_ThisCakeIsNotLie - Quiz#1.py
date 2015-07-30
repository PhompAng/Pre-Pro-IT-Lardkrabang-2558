""" W2_ThisCakeIsNotLie - Quiz#1 """
def main(temp, inputn):
    """ This is a function """
    for i in range(1, (inputn * 2) + 1):
        if i == 1:
            print(" "*((inputn * 2) - 1 - i) + "( )", end="")
        elif i == inputn * 2:
            print(" "*((inputn * 2) - 1 - i) + "|_"*(temp + 1) + "|", end="")
        elif i % 2 == 0:
            print(" "*((inputn * 2) - 1 - i) + "_|"*(temp + 2) + "_", end="")
        else:
            print(" "*((inputn * 2) - 1 - i) + "| "*(temp + 2 + 1) + "|", end="")
            temp += 2
        print("")
main(0, int(input()))
