""" Final_Hacked """
import itertools
def main():
    """ ZZzz """
    inputn = list()
    inputn.append(input())
    pattern = list(itertools.permutations(inputn[0]))
    for _ in range(len(pattern) - 2):
        inputn.append(input())
    for i in pattern:
        if "".join(i) not in inputn:
            print("".join(i))
            return 0
main()
