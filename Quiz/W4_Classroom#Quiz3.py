""" W4_Classroom#Quiz3 """
def main():
    """ WOW Timeout """
    inputn = int(input())
    chair = list()
    hand = [[0 for _ in range(inputn)] for _ in range(inputn)]
    for i in range(inputn):
        temp = []
        for _ in range(inputn):
            temp.append(int(input()))
        chair.append(temp)
        hand[i][temp.index(min(temp))] += 1
    for i in range(inputn):
        maxcolum = -9999999
        for _ in range(inputn):
            if maxcolum < chair[_][i]:
                maxcolum = chair[_][i]
        for _ in range(inputn):
            if chair[_][i] == maxcolum:
                hand[_][i] += 1
    for i in range(inputn):
        for _ in range(inputn):
            if hand[i][_] == 2:
                print(chair[i][_])
                return 0
    print("404 Not Found!")
main()
