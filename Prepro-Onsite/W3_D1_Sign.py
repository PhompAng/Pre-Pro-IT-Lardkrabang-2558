""" W3_D1_Sign """
def main():
    """ This is a function """
    inputstr = []
    for _ in range(3):
        inputstr.append(input())
    maxlen = max(list(map(len, inputstr)))
    for i in range(maxlen):
        for j in inputstr:
            if i < len(j):
                print(j[i] + " ", end="")
            else:
                print("  ", end="")
        print("")
main()
