import turtle as t

window = t.Screen()
window.setup(800, 800)
board = t.Turtle()
board.penup()
board.goto(-400, -400)
board.pendown()
y = -400
x = -400
board.speed(0)
window.register_shape("./pieces/pawn-b.gif")
window.register_shape("./pieces/pawn-w.gif")
window.register_shape("./pieces/bishop-b.gif")
window.register_shape("./pieces/bishop-w.gif")
window.register_shape("./pieces/knight-w.gif")
window.register_shape("./pieces/knight-b.gif")
window.register_shape("./pieces/rook-b.gif")
window.register_shape("./pieces/rook-w.gif")
window.register_shape("./pieces/queen-b.gif")
window.register_shape("./pieces/queen-w.gif")
window.register_shape("./pieces/king-b.gif")
window.register_shape("./pieces/king-w.gif")


color = "white"
for boxes in range(8):
    for box in range(8):
        if (boxes + box) % 2 == 0:
            board.fillcolor("black")
        else:
            board.fillcolor("white")
        board.begin_fill()
        board.forward(100)
        board.left(90)
        board.forward(100)
        board.left(90)
        board.forward(100)
        board.left(90)
        board.forward(100)
        board.left(90)
        board.end_fill()
        board.penup()
        board.forward(100)
        board.pendown()
    board.penup()
    y += 100
    board.goto(x, y)
    board.pendown()
board.hideturtle()

rook_w = t.Turtle()
rook_w.shape("./pieces/rook-w.gif")

rook_b = t.Turtle()
rook_w.shape("./pieces/rook-b.gif")
rook_b.penup()
rook_w.penup()


def drag_handler(x, y):
    rook_w.goto(x, y)
    t.update()


t.hideturtle()
rook_w.ondrag(drag_handler)

t.tracer(0)
t.done()
