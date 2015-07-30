""" WATAFAKKKKKKKKKKK """
def main():
    """ SHIP """
    inputstr = input()
    cheat = "UUDDLRLRBAS"
    for i in range(len(inputstr)):
        if inputstr[i:] in cheat and inputstr[i:] in cheat[:len(inputstr[i:])]:
            print(cheat[len(inputstr[i:]):])
            return 0
    print(cheat)
main()
