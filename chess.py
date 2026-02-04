import turtle as t
import turtle

t.penup()
t.goto(-200, -200)
t.pendown()
y = -200
x = -200
color = "white"
for boxes in range(8):
    if color == "black":
        t.fillcolor(color)
        color = "white"
    else:
        t.fillcolor(color)
        color = "black"
    for box in range(8):
        if color == "black":
            t.fillcolor(color)
            color = "white"
        else:
            t.fillcolor(color)
            color = "black"
        t.begin_fill()
        t.forward(40)
        t.left(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(40)
        t.end_fill()

    t.penup()
    y += 40
    t.goto(x, y)
    t.pendown()

turtle.done()
