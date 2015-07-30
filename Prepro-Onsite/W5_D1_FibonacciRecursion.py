""" W5_D1_FibonacciRecursion """
def res(inputn, index=0, last=0, now=1):
    """ recursion """
    return last if index >= inputn else res(inputn, index + 1, now, last + now)
print(res(int(input())))
