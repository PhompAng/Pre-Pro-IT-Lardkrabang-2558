""" W5_D1_1toN_Recur """
def main(inputn):
    """ Kongo my Waifu """
    if inputn <= 0:
        return 0
    if inputn > 1:
        return inputn + main(inputn - 1)
    return 1
print(main(int(input())))
