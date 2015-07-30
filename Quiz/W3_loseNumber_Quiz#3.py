""" W3_loseNumber_Quiz#3 """
def main():
    """ WOW """
    inputn = int(input())
    inputnum = []
    while True:
        temp = int(input())
        if temp == 0 or len(inputnum) >= inputn:
            break
        inputnum.append(temp)
    chk = 0
    inputnum.sort()
    if len(inputnum) == 0:
        for i in range(1, inputn + 1):
            print(i)
        return 0
    for i in range(1, inputn + 1):
        #print(i, chk)
        if i == inputnum[chk]:
            if chk < len(inputnum) - 1:
                chk += 1
        elif i != inputnum[chk]:
            print(i)
main()
