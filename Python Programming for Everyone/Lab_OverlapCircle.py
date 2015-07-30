""" Lab_OverlapCircle """
def main():
    """ This is function """
    psx1 = int(input())
    psy1 = int(input())
    psr1 = int(input())
    psx2 = int(input())
    psy2 = int(input())
    psr2 = int(input())
    distance = ((psx1 - psx2)**2 + (psy1 - psy2)**2)**0.5
    print(["no overlapping", "overlapping"][distance <= psr1 + psr2])
main()