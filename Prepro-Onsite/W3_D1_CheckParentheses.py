""" W3_D1_CheckParentheses """
def main():
    """ this is a function """
    count = 0
    inputn = input()
    for i in inputn:
        if i == "(":
            count += 1
        elif count == 0 and i == ")":
            count -= 2
        elif i == ")":
            count -= 1
    if count == 0:
        print("YES")
    else:
        print("NO")
main()
