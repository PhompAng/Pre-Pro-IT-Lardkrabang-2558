""" W4_D2_CaesarV1 """
def main():
    """ Kongo Kongo """
    inputn = int(input())
    upp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low = "abcdefghijklmnopqrstuvwxyz"
    inputstring = input()
    for i in inputstring:
        if i in upp:
            print(upp[((ord(i) - 65) + inputn) % 26], end="")
        elif i in low:
            print(low[((ord(i) - 97) + inputn) % 26], end="")
        else:
            print(i, end="")
main()
