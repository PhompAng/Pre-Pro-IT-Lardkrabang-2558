""" W4_D3_Safe """
def main():
    """ Kongo Kongo """
    #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    inputstring = input()
    inputlock = input()
    count = 0
    for i in range(len(inputstring)):
        if (ord(inputstring[i]) - ord(inputlock[i])) % 26 >\
         (ord(inputlock[i]) - ord(inputstring[i])) % 26:
            count += (ord(inputlock[i]) - ord(inputstring[i])) % 26
        else:
            count += (ord(inputstring[i]) - ord(inputlock[i])) % 26
    print(count)
main()
