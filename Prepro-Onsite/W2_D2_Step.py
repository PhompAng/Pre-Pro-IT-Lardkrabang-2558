""" W2_D2_Step """
def main():
    """ Nanodesu~ """
    limit, step = int(input()), int(input())
    if (limit > 1 and step > 0) and step != 0:
        for i in range(1, limit + 1, step):
            print(i)
    elif limit < 1 and step < 0:
        for i in range(1, limit - 1, step):
            print(i)
    else:
        print("error")
main()
