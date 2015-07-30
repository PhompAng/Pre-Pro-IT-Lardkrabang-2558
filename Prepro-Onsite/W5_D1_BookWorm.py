""" W5_D1_BookWorm """
def main():
    """ I forgot docstring always time """
    inputn = int(input())
    for _ in range(inputn):
        time, book = int(input()), int(input())
        timebook = list()
        total, count = 0, 0
        for _ in range(book):
            timebook.append(int(input()))
        timebook = sorted(timebook)
        for i in range(len(timebook)):
            if total + timebook[i] > time:
                break
            total += timebook[i]
            count += 1
        print(count)
main()
