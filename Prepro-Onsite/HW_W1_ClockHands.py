""" HW_W1_ClockHands """
def main(ihr, imi, lis):
    """ ihr = input hour; imi = input minutes; """
    print([False, True][((ihr == 0 or ihr == 11) and imi == 0) or (ihr * 5) + lis[ihr - 1] == imi])
main(int(input()), int(input()), [0, 0, 1, 1, 2, 2, 3, 3, 4, 4])
