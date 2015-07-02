""" W2_D1_100Times """
def res(limit=100):
    """ WOW Recursive """
    if limit != 0:
        print("Hello World!")
        res(limit - 1)
    else:
        return 0
def main():
    """ WOW wat dat """
    res()
main()
