""" W4_D2_YO_PonFire """
def main():
    """ Sawasdee Ka """
    inputnut, inputyo = input(), input()
    totalnut, totalyo = 0, 0
    for i in inputnut:
        totalnut += ord(i)
    for i in inputyo:
        totalyo += ord(i)
    if totalnut > totalyo:
        print("Yo Kakkkkkkk")
    elif totalnut < totalyo:
        print("TA Nut Kakkkkkkk")
    else:
        print("TA Nut and Yo Kakkkkkkk")
main()
