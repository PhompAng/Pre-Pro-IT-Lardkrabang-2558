""" W3_D1_Patland """
def main():
    """ ahhhhhh """
    inputn = int(input())
    inputstr = []
    for _ in range(inputn):
        inputstr.append(input())
    index = 1
    for i in inputstr:
        if i[len(i) - 1] in "aeiou" or i[len(i) - 1] in "AEIOU":
            print("Case #" + str(index) + ": " + i + " is ruled by a queen.")
        elif i[len(i) - 1] == "y" or i[len(i) - 1] == "Y":
            print("Case #" + str(index) + ": " + i + " is ruled by nobody.")
        else:
            print("Case #" + str(index) + ": " + i + " is ruled by a king.")
        index += 1
main()
