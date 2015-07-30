""" W4_D2_WeAreTheSame """
def kongo(inputn, char):
    """ Kongo desu """
    num = 0
    for i in range(len(inputn)):
        if inputn[i] == char:
            num += 1
    return num
def main():
    """ Kongo desu """
    inputn = []
    for _ in range(16):
        inputn.append(int(input()))
    inputn = sorted(inputn)
    setinputn = list(set(inputn))
    for i in setinputn:
        if kongo(inputn, i) > 1:
            print(i)
main()
