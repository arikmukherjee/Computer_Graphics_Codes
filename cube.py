import turtle
from typing import List, Tuple


def drawCoordinate(t: turtle.Turtle):
    t.seth(0); t.color((0.7,0.7,0.7), 'white')

    # Y axes
    t.pu(); t.goto(0,-H//2); t.pd()
    for _ in range(20):
        t.bk(5); t.fd(10); t.bk(5)
        t.seth(90); t.fd(H//20); t.seth(0)
    t.bk(5); t.fd(10); t.bk(5)

    # X axes
    t.pu(); t.home(); t.goto(-W//2,0); t.seth(90); t.pd()
    for _ in range(20):
        t.bk(5); t.fd(10); t.bk(5)
        t.seth(0); t.fd(W//20); t.seth(90)
    t.bk(5); t.fd(10); t.bk(5)

    # go to center & reset turtle pen
    t.pu(); t.home(); t.seth(0); t.pd()
    t.pensize(1); t.color('black', 'white')


def scale(points: List[Tuple[int, int]], x_scale: int, y_scale: int):
    spv =[]
    for (x, y) in points:
        xd = x * x_scale
        yd = y * y_scale
        spv.append((xd, yd))
    return spv


def drawPolygon(vertices: List[Tuple[int, int]]):
    t.pu()
    for i in range(len(vertices)+1):
        p = i%len(vertices)
        t.goto(vertices[p])
        t.pd()
    t.pu()


if __name__ == '__main__':
    W, H, p = 600, 600, 40

    s = turtle.Screen(); s.setup(W+p, H+p); s.tracer(False)
    t = turtle.Turtle(); t.speed(0); 
    t.hideturtle()
    drawCoordinate(t)

    # create polygon
    t.pencolor(0.8,0.8,0.8)
    pv = [(50, 50), (100, 50), (100, 100), (50, 100)]
    drawPolygon(pv)
    
    #create polygon2
    t.pencolor(0.8,0.8,0.8)
    pv = [(80, 80)]
    drawPolygon(pv)

    # scaling
    t.pencolor('black')
    spv = scale(pv, 1.5, 1.5)
    drawPolygon(spv)

    s.tracer(True)
    turtle.done()
