""" W1_D2_CirINRec """
def main():
    """ ZZzz """
    inputw, inputh = int(input()), int(input())
    inputx, inputy = int(input()), int(input())
    inputr = int(input())
    if inputx + inputr <= inputw and inputx - inputr >= 0:
        if inputy + inputr <= inputh and inputy - inputr >= 0:
            print("Yes")
            return 0
    print("No")
main()
