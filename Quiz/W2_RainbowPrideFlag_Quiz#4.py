""" W2_RainbowPrideFlag_Quiz#4 """
def main():
    """ This is a function """
    width, height = int(input()), int(input())
    wowo = height / 6
    count = 0
    if height % 6 != 0 or height == 0 or width == 0 or height < 6:
        print("Height " + str(height) + " pixel can't create pride flag.")
        return 0
    indicolor = 1
    for _ in range(height):
        print(str(indicolor)*width)
        count += 1
        if count == wowo:
            indicolor += 1
            count = 0
main()
