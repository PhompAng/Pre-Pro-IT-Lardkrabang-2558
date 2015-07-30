""" DaY_Z_ImageEditor """
def isturnright(firstinput, secondinput, inputn):
    """ is_turnright """
    firstcheck, secondcheck = list(), list()
    for i in range(inputn):
        for j in range(inputn):
            firstcheck.append(firstinput[i][j])
    for i in range(inputn - 1, -1, -1):
        for j in range(inputn):
            secondcheck.append(secondinput[j][i])
    return firstcheck == secondcheck

def isturnleft(firstinput, secondinput, inputn):
    """ is_turnleft """
    firstcheck, secondcheck = list(), list()
    for i in range(inputn):
        for j in range(inputn):
            firstcheck.append(firstinput[i][j])
    for i in range(inputn):
        for j in range(inputn - 1, -1, -1):
            secondcheck.append(secondinput[j][i])
    return firstcheck == secondcheck

def ishflip(firstinput, secondinput, inputn):
    """ is_hflip """
    firstcheck, secondcheck = list(), list()
    for i in range(inputn):
        for j in range(inputn):
            firstcheck.append(firstinput[i][j])
    for i in range(inputn - 1, -1, -1):
        for j in range(inputn):
            secondcheck.append(secondinput[i][j])
    return firstcheck == secondcheck

def isvflip(firstinput, secondinput, inputn):
    """ is_vflip """
    firstcheck, secondcheck = list(), list()
    for i in range(inputn):
        for j in range(inputn):
            firstcheck.append(firstinput[i][j])
    for i in range(inputn):
        for j in range(inputn - 1, -1, -1):
            secondcheck.append(secondinput[i][j])
    return firstcheck == secondcheck

def isinverse(firstinput, secondinput, inputn):
    """ is_inverse """
    firstcheck, secondcheck = list(), list()
    for i in range(inputn):
        for j in range(inputn):
            firstcheck.append(["#", "."][firstinput[i][j] == "#"])
    for i in range(inputn):
        for j in range(inputn):
            secondcheck.append(secondinput[i][j])
    return firstcheck == secondcheck

def main():
    """ This is a main """
    inputn = int(input())
    for _ in range(inputn):
        inputsize = int(input())
        firstinput, secondinput = list(), list()
        for _ in range(inputsize):
            firstinput.append(input())
        for _ in range(inputsize):
            secondinput.append(input())
        if isturnright(firstinput, secondinput, inputsize):
            print("turnright")
        elif isturnleft(firstinput, secondinput, inputsize):
            print("turnleft")
        elif ishflip(firstinput, secondinput, inputsize):
            print("hflip")
        elif isvflip(firstinput, secondinput, inputsize):
            print("vflip")
        elif isinverse(firstinput, secondinput, inputsize):
            print("inverse")
main()
