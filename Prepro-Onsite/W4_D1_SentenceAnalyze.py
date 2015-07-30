""" W4_D1_SentenceAnalyze """
def c0unt(inputn, char):
    """ WOW c0unt """
    num = 0
    for i in range(len(inputn)):
        if inputn[i] == char:
            num += 1
    return num

def main():
    """ WOW Minecraft """
    inputn = input().split(" ")
    inputn.sort()
    for i in sorted(list(set(inputn))):
        print(i + ":" + str(c0unt(inputn, i)))
main()
