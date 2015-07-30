""" HW_W4_YouChooselv """
def main():
    """ who care DOCSTRING again? You? but not me"""
    pokedict = dict()
    inputn = int(input())
    for _ in range(inputn):
        temp = input().split(" ")
        pokedict[temp[0]] = int(temp[1])
    check = input()
    if check.isnumeric():
        for i in pokedict:
            if pokedict[i] == int(check):
                print(i)
    else:
        print(pokedict[check])
main()
