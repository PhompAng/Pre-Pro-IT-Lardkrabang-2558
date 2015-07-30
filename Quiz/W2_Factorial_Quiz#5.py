""" W2_Factorial_Quiz#5 """
def main():
    """ This is a function """
    inputn = int(input())
    suma = 1
    for i in range(inputn, 0, -1):
        suma *= i
    print(suma)
main()
