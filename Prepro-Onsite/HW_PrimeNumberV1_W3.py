""" HW_PrimeNumberV1_W3 """
def primer(num, grid, lenn):
    """prime grid check"""
    step = grid[num]
    step = int(step)
    for xxx in range(num + step, lenn, step):
        grid[xxx] = 0

def main():
    """Calculate"""
    maxx = int(input())
    if maxx == 0 or maxx == 1 or maxx < 0:
        print(0)
        return 0
    if maxx == 2:
        print(1)
        return 0
    maxx += 1
    grid = list(range(3, maxx, 2))
    lenn = int((maxx - 2) / 2)
    count = 1
    for xxx in range(lenn):
        if grid[xxx] != 0:
            count += 1
            primer(xxx, grid, lenn)
    print(count)
main()
