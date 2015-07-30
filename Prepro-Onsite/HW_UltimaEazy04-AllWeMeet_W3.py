""" HW_UltimaEazy04-AllWeMeet_W3 """
def main():
    """ My life need minecraft """
    inputstring = input().split(" vs ")
    for i in range(len(inputstring)):
        for j in range(len(inputstring)):
            if inputstring[i] != inputstring[j]:
                print(inputstring[i], inputstring[j])
main()
