""" HW_W2_HaPaSi """
def main():
    """ ZZzz """
    count = 0
    scorea, scoreb, draw = 0, 0, 0
    while scoreb < 5 and scorea < 5 and draw != 5:
        inputn = input()
        count += 1
        if inputn[0] == inputn[4]:
            draw += 1
        else:
            draw = 0
            if "H - S" or "P - H" or "S - P":
                scorea += 1
            elif "S - H" or "H - P" or "P - S":
                scoreb += 1
    if draw == 5:
        print("NONE")
    elif scorea == 5:
        print("A")
    elif scoreb == 5:
        print("B")
    print(count)
main()
