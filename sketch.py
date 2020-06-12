from p5 import *
import random
w = 0
h = 0
width = 400
height = 400
cols = 25
rows = 25

openSet = []
closedSet = []

start = None
end = None

mode = None  # possible s e w r


class Spot:
    def __init__(self, i, j):
        self.f = 10**9
        self.g = 10**9
        self.i = i
        self.j = j
        self.prev = None
        self.wall = False

    def show(self, col):
        fill(col)
        if self.wall:
            fill(0)
        no_stroke()
        if self.wall:
            rect((self.j*h, self.i*w), w-1, h-1)
        else:
            circle((self.j*h+h/2, self.i*w+w/2), h/2+6, CENTER)

    def __str__(self):
        return f'[{self.i},{self.j}] '


grid = [[Spot(i, j) for j in range(cols)] for i in range(rows)]


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
            if grid[a][b].wall != True:
                neighbors.append(grid[a][b])  # add wall
    return neighbors


def setup():
    global w, h, start, end, openSet
    size(width, height)

    w = width//cols
    h = height//rows


start = end = current = None
path = []


def draw():
    global openSet, closedSet, grid, start, end, current, path

    if mode == 's':
        if mouse_is_pressed:
            i = floor(mouse_x/w)
            j = floor(mouse_y/h)
            try:
                start = grid[j][i]
                start.wall = False
                start.g = 0
                start.f = 0
                openSet = [start]
            except:
                pass

    elif mode == 'e':
        if mouse_is_pressed:
            i = floor(mouse_x/w)
            j = floor(mouse_y/h)
            try:
                end = grid[j][i]
                end.wall = False
            except:
                pass

    elif mode == 'w':
        if mouse_is_pressed:
            i = floor(mouse_x/w)
            j = floor(mouse_y/h)
            try:
                grid[j][i].wall = True
            except:
                pass

    elif mode == 'r':
        if len(openSet) > 0:
            current = min(openSet, key=lambda node: node.f)
            if current == end:
                no_loop()
                print("DONE")
                return
            else:
                openSet.remove(current)
                closedSet.append(current)
                neighbor = getneighbors(current)
                for i in range(len(neighbor)):
                    if neighbor[i] in closedSet:
                        continue

                    tempG = current.g+1

                    if tempG < neighbor[i].g:
                        neighbor[i].prev = current
                        neighbor[i].g = tempG
                        neighbor[i].f = neighbor[i].g + \
                            heuristic(neighbor[i], end)
                        if neighbor[i] not in openSet:
                            openSet.append(neighbor[i])

        else:
            print("NO Solution")
            no_loop()
            return

    for each_row in grid:
        for spot in each_row:
            spot.show(Color(255))
    if start != None:
        start.show(Color(0, 0, 255))
    if end != None:
        end.show(Color(255, 0, 200))

    if current != None:
        temp = current
        path = [temp]
        while temp.prev != None:
            path.append(temp.prev)
            temp = temp.prev

    for spot in path:
        spot.show(Color(0, 0, 255))


def key_pressed():
    global mode
    if mode != 'r':
        mode = str(key)


if __name__ == '__main__':
    run()
