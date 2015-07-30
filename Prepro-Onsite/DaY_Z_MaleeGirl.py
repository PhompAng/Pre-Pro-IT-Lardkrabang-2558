""" DaY_Z_MaleeGirl """
def process(pst, dist, queue, pos, lstpos):
    """

    -- process dist --
    pos is list of position, it contain psrow, psindex
    psrow = pos[0]; psindex = pos[1]
    lstpos is old position before update to next block

    """

    #alt keep distance from start point to next point
    alt = pst[pos[0]][pos[1]] + dist[lstpos[0]][lstpos[1]]

    if dist[pos[0]][pos[1]] == 0 or dist[pos[0]][pos[1]] > alt:
        dist[pos[0]][pos[1]] = alt
        queue.append([pos[0], pos[1]]) #add next point to queue

    #return dist and queue to function find route
    return [dist, queue]

def tellyourworld(row, index, pst, psrow, psindex):
    """ tellyourworld isn't important. It's Dijkstra algorithm"""

    queue = list() #queue for keep what is a next route!

    #initial table to keep distance from start point
    dist = [[0 for _ in range(index)] for _ in range(row)]

    #Add initial route [row, index]
    queue.append([0, 0])

    while len(queue) > 0:

        #pull out value from queue and remove that value
        psrow, psindex = queue[0][0], queue[0][1]
        del queue[0]

        #Add queue and calculate distance
        if psrow == row - 1 and psindex == index - 1:
            #in case we stay in destination but queue exist value
            pass
        elif psrow == row - 1:
            #gone bottom
            temp = process(pst, dist, queue, [psrow, psindex + 1], [psrow, psindex])
            dist, queue = temp[0], temp[1]
        elif psindex == index - 1:
            #stay right of map
            temp = process(pst, dist, queue, [psrow + 1, psindex], [psrow, psindex]) #go down
            dist, queue = temp[0], temp[1]
        elif psrow == 0:
            #stay top
            temp = process(pst, dist, queue, [psrow, psindex + 1], [psrow, psindex]) #go right
            dist, queue = temp[0], temp[1]
            temp = process(pst, dist, queue, [psrow + 1, psindex], [psrow, psindex]) #go down
            dist, queue = temp[0], temp[1]
        elif psindex == 0:
            #stay left of map
            temp = process(pst, dist, queue, [psrow + 1, psindex], [psrow, psindex]) #go down
            dist, queue = temp[0], temp[1]
            temp = process(pst, dist, queue, [psrow, psindex + 1], [psrow, psindex]) #go right
            dist, queue = temp[0], temp[1]
        elif psindex > 0 and psindex < index - 1 and psrow > 0 and psrow < row - 1:
            #for anywhere
            temp = process(pst, dist, queue, [psrow + 1, psindex], [psrow, psindex]) #go down
            dist, queue = temp[0], temp[1]
            temp = process(pst, dist, queue, [psrow, psindex + 1], [psrow, psindex]) #go right
            dist, queue = temp[0], temp[1]
            temp = process(pst, dist, queue, [psrow, psindex - 1], [psrow, psindex]) #go left
            dist, queue = temp[0], temp[1]
            temp = process(pst, dist, queue, [psrow - 1, psindex], [psrow, psindex]) #go up
            dist, queue = temp[0], temp[1]
    print(dist[row - 1][index - 1])
def main():
    """ This is a function ? """
    row, index = int(input()), int(input())
    pst = [[0 for _ in range(index)] for _ in range(row)] #initial table for input map

    #input map from user
    for i in range(row):
        for j in range(index):
            pst[i][j] = int(input())
    tellyourworld(row, index, pst, 0, 0)
main()
