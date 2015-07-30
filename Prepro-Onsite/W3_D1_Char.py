""" W3_D1_Char """
def main():
    """ WOW """
    inputn = input()
    lower, upper = 0, 0
    for i in inputn:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
    print(str(lower) + "\n" + str(upper) + "\n" + inputn.lower() + "\n" + inputn.upper())
main()
