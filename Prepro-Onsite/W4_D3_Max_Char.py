""" W4_D3_Max_Char """
def main():
    """ Minecraft """
    key = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0\
    , "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0\
    , "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
    inputn = int(input())
    keep = []
    for _ in range(inputn):
        string = input().upper()
        for i in key:
            key[i] += string.count(i)
        maxkey = max(key.values())
        temp = ""
        for i in key:
            temp += ["", str(i)][maxkey == key[i]]
        keep.append(temp)
        for i in key:
            key[i] = 0
    for i in keep:
        print("".join(sorted(i)))
main()
