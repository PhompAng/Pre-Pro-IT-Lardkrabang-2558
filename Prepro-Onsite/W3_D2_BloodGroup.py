""" W3_D2_BloodGroup """
def main():
    """ Hi """
    inputn = int(input())
    blooda, bloodb, bloodab, bloodo = 0, 0, 0, 0
    for _ in range(inputn):
        blood = input()
        if "AB" in blood:
            bloodab += 1
        elif "B" in blood:
            bloodb += 1
        elif "A" in blood:
            blooda += 1
        elif "O" in blood:
            bloodo += 1
    print(blooda)
    print(bloodb)
    print(bloodo)
    print(bloodab)
main()
