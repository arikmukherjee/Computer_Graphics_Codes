import turtle
t=turtle.Turtle()
t.shape("turtle")

#Square
t.left(90)
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)

#Rectangle
t.reset()
t.left(90)
t.forward(100)
t.right(90)
t.forward(250)
t.right(90)
t.forward(100)
t.right(90)
t.forward(250)

#Rhombus
t.reset()
t.forward(200)
t.left(115)
t.forward(200)
t.left(65)
t.forward(180)
t.left(110)
t.forward(200)

#Parallelogram
t.reset()
t.forward(200)
t.left(115)
t.forward(150)
t.left(65)
t.forward(200)
t.left(115)
t.forward(150)

#Triangle
t.reset()
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)

turtle.done