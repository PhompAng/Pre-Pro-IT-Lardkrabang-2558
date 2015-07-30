""" Final_Teleport """
import math
def main():
    """ ZZzz """
    inputn, cost = int(input()), input()
    if "." in cost:
        cost = float(cost)
    else:
        cost = int(cost)
    dist = list()
    for _ in range(inputn):
        temp = input()
        if "." in temp:
            dist.append(float(temp))
        else:
            dist.append(int(temp))
    for _ in range(1, inputn + 1):
        temp = dist[_ - 1]
        if "." in str(temp):
            print("Case " + str(_) + ": ", end="")
            print("%.4f" % temp, end="")
            print(" Km. - " + str(math.ceil(temp * cost)) + " Gold")
        else:
            print("Case " + str(_) + ": ", end="")
            print(temp, end="")
            print(" Km. - " + str(math.ceil(temp * cost)) + " Gold")
main()
