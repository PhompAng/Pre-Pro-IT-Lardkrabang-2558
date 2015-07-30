""" W4_D2_Ask """
def main():
    """ Kongo Hiei kirishima Haruna """
    ask = {"Walk": 0, "Car": 0, "Bus": 0, "Airplane": 0, "Warp": 0, "Paradrop": 0\
    , "Helicopter": 0, "Dig": 0, "Jetpack": 0, "Fly": 0, "Jump": 0, "Balloon": 0, "Bird": 0\
    , "Unicorn": 0, "Broom": 0, "Rocket": 0, "Kafra": 0, "Water Rocket": 0, "Blink": 0\
    , "E-mail": 0, "Internet": 0, "Banana Boat": 0, "Prone": 0, "Sprint": 0, "Dimension Door": 0\
    , "Tamiya": 0, "285": 0}
    inputn = int(input())
    for _ in range(inputn):
        ask[input()] += 1
    count = 0
    for i in ask:
        if count >= 2:
            break
        if ask[i] == max(ask.values()):
            count += 1
    if max(ask.values()) != 0 and count == 1:
        print(max(ask, key=ask.get))
    else:
        print("No.")
main()
