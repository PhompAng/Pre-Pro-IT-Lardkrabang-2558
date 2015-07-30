""" W2_LimitExceed_Quiz#3 """
def main():
    """ This is a function """
    sumn, inputn = 0, 0
    while sumn <= 1024:
        inputn = int(input())
        sumn += inputn
    print(sumn)
main()
