from p5 import *

w = 0
h = 0


class Spot:
    def __init__(self, i, j):
        self.f = 10**9
        self.g = 10**9
        self.i = i
        self.j = j
        self.prev = None

    def show(self, col):
        fill(col)
        no_stroke()
        rect((self.j*h, self.i*w), w-1, h-1)

    def __str__(self):
        return f'[{self.i},{self.j}] '


width = 400
height = 400
cols = 25
rows = 25

grid = [[Spot(i, j) for j in range(cols)] for i in range(rows)]
openSet = []
closedSet = []
# path = []
start = None
end = None


def setup():
    global w, h, start, end, openSet
    size(width, height)

    w = width//cols
    h = height//rows
    # for lis in grid:
    #     for x in lis:
    #         print(x, end="")
    #     print()
    start = grid[0][0]
    start.g=0
    start.f=0
    end = grid[13][4]
    openSet.append(start)


def heuristic(a, b):
    return abs(a.i-b.i)+abs(a.j-b.j)


def getneighbors(spot):
    adder = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    neighbors = []
    i = spot.i
    j = spot.j
    for a, b in adder:
        a += i
        b += j
        if 0 <= a < rows and 0 <= b < cols:
            neighbors.append(grid[a][b])  # add wall
    return neighbors


def draw():
    global openSet, closedSet, grid
    # if len(openSet) > 0:
    #     # keep going
    #     pass
    # else:
    #     #  no soln
    #     pass
    # ..................................
    # current=None
    if len(openSet) > 0:
        # print("while")
        current = min(openSet, key=lambda node: node.f)
        # print("curr:",current)

        if current == end:
            no_loop()
            print("DONE")
        else:
            openSet.remove(current)
            closedSet.append(current)
            neighbor = getneighbors(current)

            # print("neighbor:",end=" ")
            # for spots in neighbor:
            #     print(spots,end=" ")
            # print()

            for i in range(len(neighbor)):
                # print("n",neighbor[i].i,neighbor[i].j)
                if neighbor[i] in closedSet:
                    continue
                    # print("continue")
                tempG = current.g+1
                # print(f"tg{tempG} ng{neighbor[i].g}")
                if tempG < neighbor[i].g:
                    # print("if1")
                    neighbor[i].prev = current
                    neighbor[i].g = tempG
                    neighbor[i].f = neighbor[i].g + heuristic(neighbor[i], end)
                    if neighbor[i] not in openSet:
                        openSet.append(neighbor[i])

            # if neighbor[i] in openSet:
            #     if tempG < neighbor[i].g:
            #         neighbor[i].g = tempG
            #         neighbor[i].f = neighbor[i].g+heuristic(neighbor[i], end)
            #         neighbor[i].prev = current
            # else:
            #     neighbor[i].g = tempG
            #     neighbor[i].f = neighbor[i].g+heuristic(neighbor[i], end)
            #     neighbor[i].prev = current
            #     openSet.append(neighbor[i])
            # neighbor[i].f = neighbor[i].g+heuristic(neighbor[i], end)
            # neighbor[i].prev = current

    # ..................................
    background(0)

    for rows in grid:
        for spot in rows:
            spot.show(Color(255))

    for spot in closedSet:
        spot.show(Color(255, 0, 0))

    for spot in openSet:
        spot.show(Color(0, 255, 0))

    end.show((Color(121, 123, 255)))
    if current!=None:
        temp = current
        path = [temp]
        while temp.prev != None:
            path.append(temp.prev)
            temp = temp.prev

    for spot in path:
        spot.show(Color(0, 0, 255))


if __name__ == '__main__':
    run()
