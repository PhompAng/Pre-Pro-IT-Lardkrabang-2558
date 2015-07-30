""" W3_SMS3310_Quiz#2 """
def main():
    """ WOWS """
    btn = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["J", "K", "L"], ["M", "N", "O"], \
    ["P", "Q", "R", "S"], ["T", "U", "V"], ["W", "X", "Y", "Z"]]
    string, inputn = [], int(input())
    for _ in range(inputn):
        inputbtn, time = int(input()), int(input())
        index = 0
        if inputbtn == 1:
            while time > 0:
                time -= 1
                if len(string) > 0:
                    string = string[:len(string) - 1]
        else:
            while time > 0:
                time -= 1
                index += 1
                if index >= len(btn[inputbtn - 2]):
                    index = 0
            string.append(btn[inputbtn - 2][index - 1])
    print(["null", "".join(string)][len(string) > 0])
main()
