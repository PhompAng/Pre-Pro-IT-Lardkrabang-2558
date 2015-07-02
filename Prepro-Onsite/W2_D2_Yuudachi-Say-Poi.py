""" W2_D2_Yuudachi-Say-Poi """
def main(inputn):
    """ KILL YUUDACHI, RESPECT MY MUTSU """
    data = []
    for i in range(1, inputn + 1):
        data.append(input() + " po" + "i"*i)
    for i in data:
        print(i)
main(int(input()))
