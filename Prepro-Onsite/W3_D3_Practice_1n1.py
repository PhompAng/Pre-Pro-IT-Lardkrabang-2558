""" W3_D3_Practice_1n1 """
def main():
    """ SAWASDEE """
    inputn = int(input())
    if inputn >= 1:
        for i in range(1, inputn + 1):
            print(i)
        for i in range(inputn - 1, 0, -1):
            print(i)
    elif inputn < 1:
        for i in range(1, inputn - 1, -1):
            print(i)
        for i in range(inputn + 1, 2):
            print(i)
main()
