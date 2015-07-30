""" W4_D3_PasswordRequired """
def main():
    """ Jellopy """
    inputn = input()
    chk = {"upp": 0, "low": 0, "num": 0}
    for i in inputn:
        if i.islower():
            chk["low"] = 1
        if i.isupper():
            chk["upp"] = 1
        if i.isnumeric():
            chk["num"] = 1
    if len(inputn) >= 10 and chk["upp"] == 1 and chk["low"] == 1 and chk["num"] == 1:
        print("*"*len(inputn) + " is good password.")
    else:
        print("*"*len(inputn) + " is bad password.")
main()
