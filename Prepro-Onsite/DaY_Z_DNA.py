""" DaY_Z_DNA """
def main():
    """ WOWWOWO """
    inputn = int(input())
    print(" "*inputn + "*")
    for star in range(1, inputn + 1):
        count = 1
        for line in range(1, star + 1):
            print(" "*(inputn - line) + "*" + " "*count + "*")
            count += 2
        count -= 4
        for line in range(star - 1, 0, - 1):
            print(" "*(inputn - line) + "*" + " "*count + "*")
            count -= 2
        print(" "*inputn + "*")
main()
