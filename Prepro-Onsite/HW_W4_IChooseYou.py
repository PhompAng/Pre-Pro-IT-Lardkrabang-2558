""" HW_W4_IChooseYou """
def main():
    """ who care DOCSTRING? You? but not me"""
    pokedict = dict()
    inputn = int(input())
    for _ in range(inputn):
        temp = input().split(" ")
        pokedict[temp[0]] = int(temp[1])
    print(pokedict[input()])
main()
