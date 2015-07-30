""" W4_D2_UltimaEazy06-MamaAddDict """
def main():
    """ Giv me kongo I will giv u Mango """
    inputn = int(input())
    data = {}
    for _ in range(inputn):
        inputkey = input().split(" ")
        data[inputkey[0]] = inputkey[1]
    print(sorted(data))
    print(sorted(data.values()))
main()
