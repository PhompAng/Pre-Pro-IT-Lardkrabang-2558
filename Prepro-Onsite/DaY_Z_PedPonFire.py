""" DaY_Z_PedPonFire """
def main():
    """ Gazzzzzzzzzzz """
    inputn = int(input())
    gas = []
    for _ in range(inputn):
        gas.append(int(input()))
    gas.sort()
    inputk = int(input())
    indexped = [0 for _ in range(max(gas) + 1)]
    for i in gas:
        indexped[i] += 1
    count = 0
    for i in gas:
        if inputk-i >= 0 and inputk-i <= gas[inputn - 1]:
            if i > inputk:
                break
            if indexped[inputk - i] > 0:
                count += indexped[inputk - i]
                indexped[i] -= 1
    print(count)
main()
