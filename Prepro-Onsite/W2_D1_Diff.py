""" W2_D1_Diff """
import math
def main(start, end):
    """ WOW WHY WOW BUT WOW """
    sum1, sum2 = 0, 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            sum1 += i
        else:
            sum2 += i
    print(int(math.fabs(sum1 - sum2)))

main(int(input()), int(input()))
