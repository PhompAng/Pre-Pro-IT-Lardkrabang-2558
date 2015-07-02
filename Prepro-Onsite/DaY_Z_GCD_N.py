""" DaY_Z_GCD_N """
def main():
    """ WOW This is a main_function for recursive """
    inputn = int(input())
    number = []
    for _ in range(inputn):
        number.append(int(input()))
    count = 0
    indi = number[0] + 1
    while count != inputn:
        count = 0
        indi -= 1
        for i in number:
            if i % indi == 0:
                count += 1
    print(indi)
main()
