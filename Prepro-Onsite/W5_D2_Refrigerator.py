""" W5_D2_Refrigerator """
def main():
    """ Zeirun """
    _ = int(input())
    inputn = list(map(int, input().split(" ")))
    day = 0
    while 0 not in inputn:
        day += 1
        indexmin = inputn.index(min(inputn))
        for i in range(len(inputn)):
            if i != indexmin:
                inputn[i] -= 1
    print(day)
main()
