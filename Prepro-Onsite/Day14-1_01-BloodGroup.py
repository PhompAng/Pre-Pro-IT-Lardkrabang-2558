""" Day14-1_01-BloodGroup """
def main():
    """ Kongo Burning Love """
    inputn = int(input())
    blood = {"AB": 0, "A": 0, "B": 0, "O": 0}
    for _ in range(inputn):
        inputblood = (input().split(","))[1]
        blood[inputblood] += 1
    print(str(blood["A"]))
    print(str(blood["B"]))
    print(str(blood["O"]))
    print(str(blood["AB"]))
main()
