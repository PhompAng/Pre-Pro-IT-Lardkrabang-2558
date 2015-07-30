""" W5_D2_MarioPipe """
def func1(inputn, line):
    """ WOWO """
    for i in range(inputn):
        if line == inputn:
            print("_[ ]_", end="")
        else:
            if i % 2 == 0:
                print(" [ ]", end="")
            else:
                print("    ", end="")
def func2(inputn, line):
    """ EIEI GUMBARE """
    for i in range(inputn):
        if line == inputn:
            if i % 2 == 0:
                print("_| |", end="")
            else:
                print("_[ ]_", end="")
        else:
            if i % 2 == 0:
                print(" | |", end="")
            else:
                print(" [ ]", end="")
def main():
    """ this is a docstring """
    inputn = int(input())
    for line in range(1, inputn + 1):
        if line == 1:
            func1(inputn, line)
        elif line == 2:
            func2(inputn, line)
        elif line == inputn:
            for i in range(inputn):
                if i + 1 == inputn:
                    print("_| |_", end="")
                else:
                    print("_| |", end="")
        else:
            for i in range(inputn):
                print(" | |", end="")
        print("")
main()
