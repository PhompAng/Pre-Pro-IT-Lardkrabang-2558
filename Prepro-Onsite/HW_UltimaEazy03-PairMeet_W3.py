""" HW_UltimaEazy03-PairMeet_W3 """
def main():
    """ Minecraft is awesome """
    inputn = int(input())
    value = []
    for _ in range(inputn):
        value.append(input())
    for i in range(inputn - 1):
        print(value[i], value[i + 1])
main()
