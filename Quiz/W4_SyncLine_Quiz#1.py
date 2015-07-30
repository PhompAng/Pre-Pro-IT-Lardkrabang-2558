""" W4_SyncLine_Quiz#1 """
def main():
    """ WOW This quiz so hard """
    input1, input2 = input(), input()
    if len(input1) < len(input2):
        lenght = len(input1)
        input2 = input2[len(input2) - lenght:]
    else:
        lenght = len(input2)
        input1 = input1[len(input1) - lenght:]
    secret = 0
    for i in range(lenght):
        secret += int(input1[i]) * int(input2[i])
    print(secret)
main()
