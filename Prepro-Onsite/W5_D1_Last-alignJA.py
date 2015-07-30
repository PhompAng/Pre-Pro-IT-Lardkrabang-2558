""" W5_D1_Last-alignJA """
def checkspaceandnoting(inputn):
    """ check ! """
    for _ in range(len(inputn)):
        if inputn[_] != " ":
            return False
    return True
def iseven(temp, num):
    """ is_even """
    if len(temp) % 2 == 0:
        return ("{:>" + str(num) + "}").format(temp)
    else:
        return ("{:^" + str(num) + "}").format(temp)
def inversetitle(inputn, temp=""):
    """ wow inverse title """
    for i in inputn.title():
        if i.islower():
            temp += i.upper()
        elif i.isupper():
            temp += i.lower()
        else:
            temp += i
    return temp
def main():
    """ format is nice """
    inputn, num = input(), int(input())
    if len(inputn) > num:
        if inputn[len(inputn) - 1] in "aeiou":
            print((inputn.title())[:num])
        else:
            print((inversetitle(inputn))[:num])
    elif checkspaceandnoting(inputn):
        if len("ehere") > num:
            print("ehere"[:num])
        else:
            print(("{:^" + str(num) + "}").format("ehere"))
    elif len(inputn) <= num:
        if inputn[len(inputn) - 1] in "aeiou":
            print(iseven(inputn.title(), num))
        else:
            print(iseven(inversetitle(inputn), num))
main()
