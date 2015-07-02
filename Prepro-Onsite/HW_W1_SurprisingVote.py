""" HW_W1_SurprisingVote """
def main(total, inmax):
    """ This is a function """
    if inmax - 3 < 0:
        print("not surprising")
    elif total <= inmax + inmax + (inmax - 3):
        print("surprising")
    else:
        print("not surprising")
main(int(input()), int(input()))
