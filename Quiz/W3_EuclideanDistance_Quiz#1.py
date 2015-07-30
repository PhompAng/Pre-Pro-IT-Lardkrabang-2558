""" W3_EuclideanDistance_Quiz#1 """
def main():
    """ FUSROOOODARRRR """
    inputn = int(input())
    inputx, inputy = [], []
    for _ in range(inputn):
        temp = input().split(" ")
        inputx.append(int(temp[0]))
        inputy.append(int(temp[1]))
    count = 0
    for i in range(1, inputn):
        count += ((inputx[i] - inputx[i - 1])**2 + (inputy[i] - inputy[i - 1])**2)**0.5
        i = i - i
    print("%.2f" % count)
main()
