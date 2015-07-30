""" W3_D1_Palindrome """
def main():
    """ World of Warship """
    inputn = int(input())
    inputstr = []
    for _ in range(inputn):
        inputstr.append(input())
    for i in inputstr:
        if i == i[::-1]:
            print(i)
main()
