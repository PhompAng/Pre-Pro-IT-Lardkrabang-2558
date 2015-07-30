""" Final_HappyDay """
def main():
    """ Happy day but I am testing """
    inputn = list(map(int, input().split(",")))
    count = 0
    for i in range(len(inputn)):
        if inputn[i] >= 80:
            count += 1
        elif i != 0 and inputn[i] >= 20 and inputn[i] - inputn[i - 1] >= 10:
            count += 1
    print(count)
main()
