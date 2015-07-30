""" W2_D3_Matrix """
def main():
    """ World of warship """
    row, index = int(input()), int(input())
    inputn = []
    psindex = 0
    for _ in range(row * index):
        inputn.append(input())
    for _ in range(row):
        for _ in range(index):
            print(inputn[psindex] + " ", end="")
            psindex += 1
        print("")
main()
