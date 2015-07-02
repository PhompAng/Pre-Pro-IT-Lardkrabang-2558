""" W2_D1_Parallelism_for_Admission """
def main():
    """ giv me mana, i will giv u MANGO!! """
    inx1, iny1 = int(input()), int(input())
    inx2, iny2 = int(input()), int(input())
    inx3, iny3 = int(input()), int(input())
    inx4, iny4 = int(input()), int(input())
    if iny2 - iny1 == 0 or iny4 - iny3 == 0:
        mm1 = (iny2 - iny1) / (inx2 - inx1)
        mm2 = (iny4 - iny3) / (inx4 - inx3)
        if mm2 == mm1:
            print("YES")
        else:
            print("NO")
    else:
        mm1 = (inx2 - inx1) / (iny2 - iny1)
        mm2 = (inx4 - inx3) / (iny4 - iny3)
        if mm2 == mm1:
            print("YES")
        else:
            print("NO")
main()
