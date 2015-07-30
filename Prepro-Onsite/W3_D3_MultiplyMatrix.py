""" W3_D3_MultiplyMatrix """
def main():
    """ Sawasdee Krub """
    inputp, inputq, inputr = int(input()), int(input()), int(input())
    inputa = [[0 for _ in range(inputq)] for _ in range(inputp)]
    inputb = [[0 for _ in range(inputr)] for _ in range(inputq)]
    for i in range(inputp):
        for j in range(inputq):
            inputa[i][j] = int(input())
    for i in range(inputq):
        for j in range(inputr):
            inputb[i][j] = int(input())
    for i in range(inputp):
        for j in range(inputr):
            temp = 0
            for k in range(inputq):
                temp += inputa[i][k] * inputb[k][j]
            print(temp, end=" ")
        print("")
main()
