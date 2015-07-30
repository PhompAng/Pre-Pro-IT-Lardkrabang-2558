""" W3_Operation_ K_Quiz#5 """
def main():
    """ WOWS """
    inputn = int(input())
    typeship = {"DD": 0.5, "CL": 1, "CT": 1.5, "AV": 2}
    for _ in range(inputn):
        repairtime, resource = 0, 0
        totalresource, totalrepairtime = 0, 0
        maxrepairtime, maxresource = -99999999, -999999999
        node = int(input())
        for _ in range(6):
            ship = input().split(' ')
            ship[2], ship[3], ship[4], ship[5] = map(int, ship[2:])
            temp = ((ship[2] * 10) * typeship[ship[1]] + (int(ship[2] / 10) * 3) + 30)
            repairtime = int((ship[3] * temp) / 60)
            resource = (ship[4] * node) + (ship[5] * node)
            totalrepairtime += repairtime
            totalresource += resource
            if maxresource < resource:
                maxresource = resource
                namemaxresource = ship[0]
            if maxrepairtime < repairtime:
                maxrepairtime = repairtime
                namemaxrepairtime = ship[0]
        print("Total repair times =", totalrepairtime)
        print("Total resource costs =", totalresource)
        print(namemaxrepairtime, "don't sleep in bathroom nya!")
        print(namemaxresource, "don't eat like Akagi nya nya!!\n")
main()