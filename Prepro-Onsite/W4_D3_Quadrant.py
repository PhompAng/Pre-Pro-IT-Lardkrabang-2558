""" W4_D3_Quadrant """
def main():
    """ Why malee girl don't use uber car? """
    inputx, inputy = int(input()), int(input())
    if inputx == 0 and inputy == 0:
        print("O")
    elif inputx > 0 and inputy > 0:
        print("Q1")
    elif inputx < 0 and inputy > 0:
        print("Q2")
    elif inputx < 0 and inputy < 0:
        print("Q3")
    elif inputx > 0 and inputy < 0:
        print("Q4")
    elif inputx == 0:
        print("Y")
    elif inputy == 0:
        print("X")
main()
