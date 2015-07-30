""" W5_D2_LoopLike """
def main():
    """ ZZzz """
    _ = int(input())
    like = list(map(int, input().split(" ")))
    count = list()
    for i in like:
        count.append(like.count(i))
    maxlike = max(count)
    aaa = list()
    for i in range(len(like)):
        if count[i] == maxlike and like[i] not in aaa:
            aaa.append(like[i])
    aaa = sorted(aaa)
    print(" ".join(list(map(str, aaa))))
main()
