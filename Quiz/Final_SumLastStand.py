""" Final_SumLastStand """
def main():
    """ ZZzz """
    inputn = int(input())
    count = 0
    for _ in range(inputn):
        num = int(input())
        count += num % 10
    print(count)
main()
