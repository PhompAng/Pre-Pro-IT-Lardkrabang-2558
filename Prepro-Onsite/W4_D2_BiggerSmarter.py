""" W4_D2_BiggerSmarter """
def main():
    """ That's Chang """
    chang = {}
    temp = [0, 0]
    inputn = input()
    while inputn != "0,0":
        inputn = inputn.split(",")
        if "." in inputn[0]:
            temp[0] = float(inputn[0])
        else:
            temp[0] = int(inputn[0])
        if "." in inputn[1]:
            temp[1] = float(inputn[1])
        else:
            temp[1] = int(inputn[1])
        chang[temp[0]] = temp[1]
        inputn = input()
    keychang = sorted(chang)
    for i in range(1, len(keychang)):
        if chang[keychang[i]] <= chang[keychang[i - 1]]:
            print("I was wrong.")
            return 0
    print("GodLike !!!")
main()
