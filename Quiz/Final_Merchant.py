""" Final_Merchant """
def main():
    """ ZZzz """
    inputn = int(input())
    divisionfive, temp, result = int(inputn / 5), inputn, 0
    while temp != 0:
        result, temp = 0, inputn
        if divisionfive > 0:
            result, temp = result + divisionfive, temp - (5 * divisionfive)
        result, temp = result + int(temp / 3), temp % 3
        if divisionfive <= 0 and temp % 3 != 0:
            print("-1")
            return 0
        divisionfive -= 1
    print(result)
main()
