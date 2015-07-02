""" W2_D3_OXFigure """
def main(inputw, inputh, inputox):
    """ dsj;sfklfasfjklsfl """
    for _ in range(inputh):
        for i in range(inputox, inputw + inputox):
            print(["X", "O"][i % 2 == 0], end="")
        inputox = [0, 1][inputox % 2 == 0]
        print("")
main(int(input()), int(input()), int(input()))
