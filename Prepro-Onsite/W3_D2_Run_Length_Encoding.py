""" W3_D2_Run_Length_Encoding """
def main():
    """ Lazyyyyyy """
    inputstr = input()
    temp = inputstr[0]
    count = 0
    for i in inputstr:
        if i == temp:
            count += 1
        else:
            print(str(count) + temp, end="")
            temp = i
            count = 1
    print(str(count) + temp, end="")
main()
