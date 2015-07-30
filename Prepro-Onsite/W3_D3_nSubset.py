""" W3_D3_nSubset """
def main():
    """ Hey man """
    inputn = input()
    print([2**len(inputn.split(",")), 1][inputn == "{}"])
main()
