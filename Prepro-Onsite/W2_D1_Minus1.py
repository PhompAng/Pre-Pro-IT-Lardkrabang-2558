""" W2_D1_Minus1 """
import math
def main(suma):
    """ wowo """
    inputa = 0
    while inputa != -1:
        suma += inputa
        inputa = input()
        if inputa == "Pi":
            inputa = math.pi
        elif inputa == "e":
            inputa = math.e
        else:
            inputa = int(inputa)
    print(suma)
main(0)
