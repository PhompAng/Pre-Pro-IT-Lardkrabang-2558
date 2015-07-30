""" W2_D3_Windmill """
def main(inputn):
    """ cdkgcdjkglcdpkfg """
    for line in range(1, inputn + 1):
        print("*"*line + " "*(inputn - line) + "*"*(inputn - line + 1))
    for line in range(1, inputn + 1):
        print(" "*(inputn - line) + "*"*line + " "*(line - 1) + "*"*(inputn - line + 1))
main(int(input()))
