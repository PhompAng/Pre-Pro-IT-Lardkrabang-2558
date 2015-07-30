""" W4_D2_Restuarant """
import math
def main():
    """ Kongo, Where are U? """
    menu = ["Fish and Chips", "Hamburger", "Spaghetti Carbonara", "Spaghetti Meatball", "Lasagna"\
    , "Garlic Bread", "Water", "Ice"]
    cost = [69, 79, 85, 70, 80, 40, 15, 3]
    order = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    while True:
        inputn = int(input())
        if inputn == 0:
            break
        if inputn >= 1 and inputn <= 8:
            order[inputn] += 1
    subtotal = 0
    for i in range(1, 9):
        if order[i] != 0:
            print(menu[i - 1] + " (" + str(order[i]) + ")  " + str(cost[i - 1] * order[i]))
            subtotal += cost[i - 1] * order[i]
    print("Subtotal " + str(subtotal))
    print("Total (VAT 7%) " + str(math.ceil(subtotal * 1.07)))
main()
