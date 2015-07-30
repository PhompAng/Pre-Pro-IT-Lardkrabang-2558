""" Final_Hamburger """
def main():
    """ Kongo Desu """
    left, right = int(input()), int(input())
    size = (left + right) * 2
    print("|"*left + "*"*size + "|"*right)
main()
