""" W2_D2_FizzBuzz """
def main(inputa, inputb, inputn):
    """ WOW no recursive """
    for i in range(1, inputn + 1):
        if i % inputa == 0 and i % inputb == 0:
            print("FB ", end="")
        elif i % inputa == 0:
            print("F ", end="")
        elif i % inputb == 0:
            print("B ", end="")
        else:
            print(str(i) + " ", end="")

main(int(input()), int(input()), int(input()))
