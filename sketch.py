from p5 import *

w = 0
h = 0


class Spot:
    def __init__(self, x, y):
        self.f = 0
        self.g = 0
        self.h = 0
        self.x = x
        self.y = y

    def show(self,col):
        fill(col)
        no_stroke()
        rect((self.x*w, self.y*h), w-1, h-1)

width=400
height=400
cols = 5
rows = 5
grid = [[Spot(i,j) for i in range(cols)] for j in range(rows)]
openSet = []
closedSet = []
start = None
end = None


def setup():
    global w,h,start,end,openSet
    size(width, height)

    w = width//cols
    h = height//rows

    start = grid[0][0]
    end = grid[rows-1][cols-1]
    openSet.append(start)


def draw():
    if len(openSet) > 0:
        # keep going
        pass
    else:
        #  no soln
        pass

    background(0)
    for rows in grid:
        for spot in rows:
            spot.show(Color(255))
    for x in openSet:
        x.show(Color(255,0,0))
    for x in openSet:
        x.show(Color(0,255,0))

if __name__ == '__main__':
    run()
