""" HW_W2_BrickBridge """
def main():
    """ ZZzz """
    small, large, goal = int(input()), int(input()), int(input())
    temp = small
    while large > 0 and goal > 0 and goal - 5 >= 0:
        goal -= 5
        large -= 1
    while small > 0 and goal > 0:
        goal -= 1
        small -= 1
    if goal > 0 or goal < 0:
        print("-1")
    else:
        print(temp - small)

main()
