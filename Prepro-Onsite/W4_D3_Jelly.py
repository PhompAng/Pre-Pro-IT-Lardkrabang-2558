""" W4_D3_Jelly """
def main():
    """ Jellopy """
    count = 0
    inputn = list(map(int, input().split(" ")))
    while inputn[0] + inputn[1] + inputn[2] != 3:
        indexmax = inputn.index(max(inputn))
        if inputn[indexmax] % 2 != 0:
            inputn[indexmax] -= 1
        inputn[indexmax] /= 2
        count += 1
    print(count)
main()
