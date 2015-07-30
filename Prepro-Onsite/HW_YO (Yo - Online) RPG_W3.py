""" HW_YO (Yo - Online) RPG_W3 """
def main():
    """ Minecraft """
    while True:
        inputn = int(input())
        if inputn > 1:
            break
    totalstr, totalagi, totalint, totalvit = 0, 0, 0, 0
    name = []
    for _ in range(inputn):
        value = input().split(" ")
        name.append(value[0])
        totalstr += int(value[1])
        totalagi += int(value[2])
        totalint += int(value[3])
        totalvit += int(value[4])
    boss = list(map(int, input().split(" ")))
    if totalstr >= boss[0] and totalagi >= boss[1] and totalint >= boss[2] and totalvit >= boss[3]:
        print("YO Kakkkkkkk")
    else:
        for i in range(len(name) - 2):
            print(name[i] + ", ", end="")
        print(name[inputn - 2] + " and " + name[inputn - 1] + " Kakkkkkkk")
main()
