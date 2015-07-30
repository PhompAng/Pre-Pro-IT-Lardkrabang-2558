""" W5_D1_LimitExceed_version2 """
def main():
    """ ZZzz """
    numstd, random = int(input()), int(input())
    std = list()
    total = 0
    for _ in range(numstd):
        std.append(int(input()))
    for i in range(numstd):
        total += std[i]
        if total >= random:
            print(i + 1, total)
            return 0
    print("none")
main()
