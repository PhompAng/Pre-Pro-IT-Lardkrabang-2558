""" W5_D2-Factorial-ial-ial!!! """
def main():
    """ menome """
    inputn, num = int(input()), len(input())
    if inputn == 0:
        print(1)
        return 0
    if inputn % num == 0:
        limit = num
    else:
        limit = inputn % num
    varn, total, result = 0, 1, 9999
    while result > limit:
        result = inputn - (varn * num)
        total *= result
        varn += 1
    print(total)
main()
