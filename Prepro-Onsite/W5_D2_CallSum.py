""" W5_D2_CallSum """
def main(limit, step, total=0, index=1):
    """ this is a main function """
    if limit == 1:
        return 1
    elif step > 0 and limit > 1 and index <= limit:
        return main(limit, step, total + index, index + step)
    elif step < 0 and limit < 1 and index >= limit:
        return main(limit, step, total + index, index + step)
    elif (step < 0 and limit < 1 and index < limit) or (step > 0 and limit > 1 and index > limit):
        return total
    elif step == 0 or (step < 0 and limit > 1) or (step > 0 and limit < 1):
        return "Error"
    else:
        return total
print(main(int(input()), int(input())))
