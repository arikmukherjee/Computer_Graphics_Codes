
import turtle

t=turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=800, height=600)
t.speed(5)
t.pensize(3)

def draw_A():
    t.penup()
    t.goto(-350,220)
    t.pendown()
    t.rt(120)
    t.circle(5,180)
    t.fd(80)
    t.right(160)
    t.fd(70)
    t.bk(10)
    t.left(190)
    t.fd(10)
    t.circle(15,292)
    t.fd(20)

def draw_B():
    t.penup()
    t.goto(-300,220)
    t.pendown()
    t.rt(120)
    t.circle(5,180)
    t.fd(80)
    t.penup()
    t.goto(-300,280)
    t.circle(-12,180)
    t.pendown()
    t.rt(110)
    t.circle(-17,300)




draw_B()
t.hideturtle()
screen.mainloop()