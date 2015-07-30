""" HW_UltimaEazy05-WhoMost_W3 """
def main():
    """ Minecrafr is my life """
    inputn = int(input())
    vote, count = [], []
    for _ in range(inputn):
        vote.append(input())
    for i in vote:
        count.append(vote.count(i))
        #print(vote.count(i), i)
    print(vote[count.index(max(count))] + "\n" + str(max(count)), end="")
main()
