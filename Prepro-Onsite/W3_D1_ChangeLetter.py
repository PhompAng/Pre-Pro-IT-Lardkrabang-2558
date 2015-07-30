""" W3_D1_ChangeLetter """
def main(inputn, inputchar, inputindex):
    """ Hi """
    if inputindex > len(inputn) or inputindex - 1 < 0:
        print("Error")
    else:
        print(inputn.replace(inputn[inputindex - 1], inputchar, 1))
main(input(), input(), int(input()))
