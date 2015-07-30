""" xXNoscope_D@y_z_H@Nz01_TrickshotXx """
def hanoi(ndisks, start, end):
    """ ANNNNAAA """
    if ndisks:
        hanoi(ndisks-1, start, 6-start-end)
        print("%d %d" % (start, end))
        hanoi(ndisks-1, 6-start-end, end)

def main():
    """ This is a hanoi """
    inputn = int(input())
    hanoi(inputn, 1, 3)
main()
