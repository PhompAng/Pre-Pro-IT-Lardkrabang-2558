""" W3_D2_ScaleMatrix """
def main():
    """ World of warship """
    row, index = int(input()), int(input())
    inputn = []
    psindex = 0
    for _ in range(row * index):
        inputn.append(float(input()))
    maxinput, mininput = max(inputn), min(inputn)
    for i in range(row * index):
        inputn[i] = (inputn[i] - mininput) / (maxinput - mininput)
    for _ in range(row):
        for _ in range(index):
            print("%.2f " % inputn[psindex], end="")
            psindex += 1
        print("")
main()
