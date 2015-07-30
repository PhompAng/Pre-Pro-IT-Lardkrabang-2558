""" W4_BestWord#Quiz2 """
def main():
    """ WOW Timeout """
    inputn = int(input())
    preprint = list()
    for _ in range(inputn):
        numword = int(input())
        score, word = [0 for _ in range(numword)], list()
        for i in range(numword):
            word.append(input())
        for i in range(len(word)):
            for j in range(len(word[i])):
                if word[i][j] in "EAIONRTLSU":
                    score[i] += 1
                elif word[i][j] in"DG":
                    score[i] += 2
                elif word[i][j] in"BCMP":
                    score[i] += 3
                elif word[i][j] in"FHVWY":
                    score[i] += 4
                elif word[i][j] in"K":
                    score[i] += 5
                elif word[i][j] in"JX":
                    score[i] += 8
                elif word[i][j] in"QZ":
                    score[i] += 10
        preprint.append(word[score.index(max(score))])
    for _ in preprint:
        print(_)
main()
