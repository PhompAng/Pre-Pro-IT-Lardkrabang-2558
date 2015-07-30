""" W4_D3_Gene """
def main():
    """ WOW Minecraft """
    string, virus = input(), input()
    temp = virus
    for i in range(len(virus)):
        print("Type " + str(i + 1) + " : " + temp)
        if temp in string:
            string = string.replace(temp, "$"*len(virus))
        temp = temp[1:len(virus)] + temp[0]
    print("Result : " + string)
main()
