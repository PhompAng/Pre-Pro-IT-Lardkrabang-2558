""" W3_D2_DeepLenV0 """
def main(inp):
    """ HI """
    print([str(inp.count(",") + 1), 0][len(inp) == 0 or inp == "[]"])
main(input())
