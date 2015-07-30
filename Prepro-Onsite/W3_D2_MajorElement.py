""" W3_D2_MajorElement """
def main():
    """ NOOB Fubuki """
    inputstr = input()
    inputstr = list(map(int, inputstr.split(",")))
    check = list(set(inputstr))
    chkmax = inputstr.count(check[0])
    chkstr = inputstr[0]
    for i in check:
        if inputstr.count(i) > chkmax:
            chkmax = inputstr.count(i)
            chkstr = i
    if inputstr.count(chkstr) > len(inputstr) / 2:
        print(str(chkstr))
    else:
        print("None")
main()
