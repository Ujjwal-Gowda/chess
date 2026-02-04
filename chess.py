import turtle as t
import turtle

t.penup()
t.goto(-200, -200)
t.pendown()
y = -200
x = -200
for boxes in range(8):
    for box in range(8):
        t.forward(40)
        t.left(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(40)

    t.penup()
    y += 40
    t.goto(x, y)
    t.pendown()
