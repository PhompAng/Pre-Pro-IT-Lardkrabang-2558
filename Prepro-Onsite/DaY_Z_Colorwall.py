""" DaY_Z_colorwall """
def changemywall(inputwall, inputsize):
    """ Drop color to your home """
    wall = []
    for i in range(inputsize[1]):
        temp = []
        for j in range(inputsize[0]):
            temp.append(inputwall[i][j])
        wall.append(temp)
    return wall

def tellyourworld(inputxy, dropcolor, color, inputsize, wall):
    """ Tell your world to Tell your wall """
    wall[inputxy[1]][inputxy[0]] = color
    if inputxy[1] > 0 and wall[inputxy[1] - 1][inputxy[0]] == dropcolor:
        wall = tellyourworld([inputxy[0], inputxy[1] - 1], dropcolor, color, inputsize, wall)
    if inputxy[1] < inputsize[1] - 1 and wall[inputxy[1] + 1][inputxy[0]] == dropcolor:
        wall = tellyourworld([inputxy[0], inputxy[1] + 1], dropcolor, color, inputsize, wall)
    if inputxy[0] > 0 and wall[inputxy[1]][inputxy[0] - 1] == dropcolor:
        wall = tellyourworld([inputxy[0] - 1, inputxy[1]], dropcolor, color, inputsize, wall)
    if inputxy[0] < inputsize[0] - 1 and wall[inputxy[1]][inputxy[0] + 1] == dropcolor:
        wall = tellyourworld([inputxy[0] + 1, inputxy[1]], dropcolor, color, inputsize, wall)
    return wall

def main():
    """ function """
    inputsize = list(map(int, input().split(" ")))
    inputwall = []
    for _ in range(inputsize[1]):
        inputwall.append(input())
    inputxy = list(map(int, input().split(" ")))
    wall = changemywall(inputwall, inputsize)
    color = input()
    dropcolor = wall[inputxy[1]][inputxy[0]]
    wall = tellyourworld(inputxy, dropcolor, color, inputsize, wall)
    for i in range(inputsize[1]):
        wall[i] = "".join(wall[i])
        for j in range(inputsize[0]):
            print(wall[i][j], end="")
        print("")
main()
