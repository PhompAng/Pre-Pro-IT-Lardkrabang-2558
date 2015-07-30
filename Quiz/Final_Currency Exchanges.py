""" Final_Currency Exchanges """
def main():
    """ ZZzz """
    curr = {"USD": [31.8, 32.7], "EUR": [40.1, 40.8], "GBP": [51, 51.55], "AUD": [26.75, 27.2]\
    , "JPY": [0.275, 0.281], "CNY": [4, 5.28], "TWD": [1.07, 1.095], "SGD": [24.65, 25.05]\
    , "KRW": [0.026, 0.03], "HKD": [4.19, 4.25], "MYR": [8.9, 9.45], "SEK": [4.05, 4.35]\
    , "CHF": [33.4, 34], "NZD": [25.2, 25.8], "CAD": [28, 28.9], "NOK": [4.15, 4.47]\
    , "DKK": [5.15, 5.47], "PHP": [0.3, 0.75], "VAM": [0.00148, 0.00157]\
    , "IDR": [0.00255, 0.00285], "INR": [0.3, 0.55]}
    wallet = {"THB": 0, "USD": 0, "EUR": 0, "GBP": 0, "AUD": 0, "JPY": 0, "CNY": 0, "TWD": 0, \
    "SGD": 0, "KRW": 0, "HKD": 0, "MYR": 0, "SEK": 0, "CHF": 0, "NZD": 0, "CAD": 0, "NOK": 0, \
    "DKK": 0, "PHP": 0, "VAM": 0, "IDR": 0, "INR": 0}
    wallet["THB"] = int(input())
    inputn = int(input())
    for _ in range(inputn):
        order = input().split(" ")
        order[2] = int(order[2])
        if order[0] == "BUY":
            tempcurr = curr[order[1]]
            if order[2] * tempcurr[1] > wallet["THB"]:
                order[2] = int(wallet["THB"] / tempcurr[1])
            wallet["THB"] -= order[2] * tempcurr[1]
            wallet[order[1]] += int(order[2])
        elif order[0] == "SELL":
            if order[2] > wallet[order[1]]:
                order[2] = wallet[order[1]]
            wallet[order[1]] -= order[2]
            tempcurr = curr[order[1]]
            wallet["THB"] += order[2] * tempcurr[0]
    for i in sorted(wallet):
        if wallet[i] >= 1:
            print(i, "%.2f" % wallet[i])
main()
