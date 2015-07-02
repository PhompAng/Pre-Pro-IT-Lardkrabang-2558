""" W2_D3_VeryBasicSort """
def main():
    """ WOWO """
    inputn = int(input())
    number = []
    for _ in range(inputn):
        number.append(int(input()))
    print("\n".join(map(str, sorted(number))))

main()
