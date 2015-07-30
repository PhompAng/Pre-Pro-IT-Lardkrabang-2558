""" W3_D2_Tanabata """
def main():
    """ This is a function """
    inputstr = input()
    inputstr = inputstr.split(".")
    print("_|_ "*len(inputstr))
    for i in range(max(list(map(len, inputstr)))):
        for j in inputstr:
            if i < len(j):
                print("|" + j[i] + "| ", end="")
            elif i >= len(j):
                print("| | ", end="")
        print("")
    print("|_| "*len(inputstr))
main()
