""" W2_D3_MinusV3 """
import math
def main(suma, inputa):
    """ wowo """
    while inputa != "-1":
        if inputa.lower() == "pi":
            inputa = math.pi
        elif inputa.lower() == "e":
            inputa = math.e
        elif "." in inputa:
            inputa = float(inputa)
        else:
            inputa = int(inputa)
        suma += inputa
        inputa = input()
    print(suma)
main(0, "0")
