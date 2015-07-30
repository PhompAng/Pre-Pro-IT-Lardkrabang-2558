""" HW_W4_Roman5000 """
def iskey(inputn, roman):
    """ Return True if inputn exist in key """
    for i in roman:
        if i == inputn:
            return True
    return False
def main():
    """ don't care """
    roman = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40\
    , "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
    inputn = input()
    index, arabic = 0, 0
    while index < len(inputn):
        if iskey(inputn[index:index + 2], roman):
            arabic += roman[inputn[index:index + 2]]
            index += 1
        else:
            arabic += roman[inputn[index]]
        index += 1
    print(arabic)
main()
