""" W2_D2_NumberStair """
def main():
    """ this is a function """
    inputn = int(input())
    j, temp = 0, 1
    if inputn <= 0:
        return 0
    for i in range(1, 10000):
        count = 1
        for j in range(temp, inputn + 1):
            print(str(j) + " ", end="")
            if count == i:
                print("")
                break
            count += 1
        if j == inputn:
            return 0
        temp = j + 1
main()
