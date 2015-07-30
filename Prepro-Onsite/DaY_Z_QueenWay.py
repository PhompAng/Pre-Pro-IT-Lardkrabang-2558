""" DaY_Z_QueenWay """
def main():
    """ World of warship """
    inputx = input()
    inputy, inputx = int(inputx[0]), int(inputx[2])
    print("-----------------")
    for line in range(-inputy, 8 - inputy):
        for row in range(8):
            if line == 0 and row == inputx:
                print("|Q", end="")
            elif line == 0 or row in [inputx - abs(line), inputx, inputx + abs(line)]:
                print("|x", end="")
            else:
                print("| ", end="")
        print("|\n-----------------")
main()