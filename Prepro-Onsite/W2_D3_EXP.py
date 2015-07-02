""" W2_D3_EXP """
def main():
    """ This is a function """
    name = input()
    exp = int(input())
    limit, lvl = 0, 0
    while exp >= limit:
        limit += 50 * ((lvl**2) + (5 * lvl) + 4)
        lvl += 1
    if lvl == 0:
        lvl += 1
        limit = 200
    print("[Lv." + str(lvl - 1) + "] " + name)
    print("Exp: " + str(exp) + " / " + str(limit))

main()
