""" W3_Search1_Quiz#4 """
def main():
    """ WOWS """
    inputn = int(input())
    inputnum = []
    for _ in range(inputn):
        inputnum.append(int(input()))
    find = int(input())
    found = []
    for i in range(inputn):
        if inputnum[i] == find:
            found.append(i)
            i = i - i
    if len(found) == 0:
        print("Data not Found.")
    elif len(found) == 1:
        print("Found at : " + str(found[0] + 1) + ".")
    else:
        print("Found at : ", end="")
        for i in range(len(found) - 1):
            print(str(found[i] + 1) + ",", end="")
            i = i - i
        print(str(found[len(found) - 1] + 1) + ".")
main()
