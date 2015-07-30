""" W4_D1_Gram_v1 """
def main():
    """ Minecraft is awesome """
    inputn = input()
    pattern_not_set = []
    for i in range(1, len(inputn)):
        pattern_not_set.append(inputn[i - 1: i + 1])
    pattern = list(set(pattern_not_set))
    dictpattern = {}
    for i in pattern:
        dictpattern[i] = 0
    for i in range(1, len(inputn)):
        dictpattern[inputn[i - 1: i + 1]] += 1
    for i in pattern_not_set:
        if dictpattern[i] == max(dictpattern.values()):
            print(i)
            break
    print(max(dictpattern.values()))
main()
