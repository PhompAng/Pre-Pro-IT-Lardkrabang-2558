""" W3_D3_Robot1000 """
def main():
    """ World of warship """
    inputn = input()
    psx, psy = 0, 0
    for i in inputn:
        if i == "N":
            psy += 1
        elif i == "S":
            psy -= 1
        elif i == "E":
            psx += 1
        elif i == "W":
            psx -= 1
        elif i == "Z":
            psx, psy = 0, 0
    print(psx, psy)
main()
