""" HW_SimpleSort_W3 """
def main():
    """ Sublime-sound """
    inputn = input().split(" ")
    for i in range(len(inputn)):
        if "." in inputn[i]:
            inputn[i] = float(inputn[i])
        else:
            inputn[i] = int(inputn[i])
    inputn.sort()
    for i in inputn:
        if i % 1 == 0:
            print(str(i) + " ", end="")
        else:
            print("%.3f " % i, end="")
main()
