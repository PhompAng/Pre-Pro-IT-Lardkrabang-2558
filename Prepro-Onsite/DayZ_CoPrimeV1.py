""" DayZ_CoPrimeV1.py """
def main():
    """ Hi, World """
    inputa, inputb = int(input()), int(input())
    division = inputa
    while inputa % division != 0 or inputb % division != 0:
        division -= 1
    if division == 1:
        print("YES\n" + str(division))
    else:
        print("NO\n" + str(division))
main()
