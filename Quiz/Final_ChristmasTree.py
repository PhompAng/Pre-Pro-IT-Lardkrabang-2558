""" Final_ChristmasTree """
def main():
    """ ZZzz """
    inputn, inputk = int(input()), int(input())
    count = 1
    for line in range(1, inputn + 1):
        print(" "*(inputn - line) + "*"*count)
        count += 2
    count -= 2
    for line in range(1, inputk + 1):
        print(" "*int((count - 3) / 2) + "---" + " "*int((count - 3) / 2))
main()
