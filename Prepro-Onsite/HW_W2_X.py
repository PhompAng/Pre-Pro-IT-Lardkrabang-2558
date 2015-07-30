""" HW_W2_X """
def main():
    """ ZZzz """
    inputn = int(input())
    temp = 0
    for line in range(1, inputn):
        print(" "*(line - 1) + "*" + " "*((inputn * 2) - 3 - temp) + "*")
        temp += 2
    print(" "*(inputn - 1) + "*")
    temp -= 3
    for line in range(inputn - 1, 0, -1):
        print(" "*(line - 1) + "*" + " "*((inputn * 2) - 4 - temp) + "*")
        temp -= 2

main()
