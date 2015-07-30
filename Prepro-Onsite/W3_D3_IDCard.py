""" W3_D3_IDCard """
def main():
    """ YAMATOOOOOO """
    inputn, num = input(), []
    for i in inputn:
        if i != "-" and i != "X":
            num.append(int(i))
    count, index = 0, 1
    for i in num:
        count += (14 - index) * i
        print(i, count)
        index += 1
    temp = count % 11
    temp = [11 - temp, 1 - temp][temp <= 1]
    index = 0
    for i in num:
        print(i, end="")
        if index == 0 or index == 4 or index == 9 or index == 11:
            print("-", end="")
        index += 1
    print(temp)
main()
