""" W2_D1_10-Count """
def res(value):
    """ WOW RECURSIVE """
    if value[2] != 0:
        if int(input()) % 2 == 0:
            value[0] += 1
        else:
            value[1] += 1
        value[2] -= 1
        return res(value)
    else:
        return value

def main(inputn):
    """ WOW WHY WOW BUT WOW """
    value = res([0, 0, inputn])
    print(str(value[0]) + "\n" + str(value[1]))

main(int(input()))
