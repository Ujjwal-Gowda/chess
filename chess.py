import turtle as t

window = t.Screen()
window.setup(800, 800)
t.tracer(0)
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
board.penup()
board.hideturtle()

rook_w = t.Turtle()
rook_w.shape("./pieces/rook-w.gif")
rook_w.penup()

rook_b = t.Turtle()
rook_b.shape("./pieces/rook-b.gif")
rook_b.penup()


bishop_w = t.Turtle()
bishop_w.shape("./pieces/bishop-w.gif")
bishop_w.penup()


bishop_b = t.Turtle()
bishop_b.shape("./pieces/bishop-b.gif")
bishop_b.penup()

knight_b = t.Turtle()
knight_b.shape("./pieces/knight-b.gif")
knight_b.penup()

knight_w = t.Turtle()
knight_w.shape("./pieces/knight-w.gif")
knight_w.penup()

king_w = t.Turtle()
king_w.shape("./pieces/king-w.gif")
king_w.penup()

king_b = t.Turtle()
king_b.shape("./pieces/king-b.gif")
king_b.penup()

queen_b = t.Turtle()
queen_b.shape("./pieces/queen-b.gif")
queen_b.penup()

queen_w = t.Turtle()
queen_w.shape("./pieces/queen-w.gif")
queen_w.penup()

pawn_w = t.Turtle()
pawn_w.shape("./pieces/pawn-w.gif")
pawn_w.penup()

pawn_b = t.Turtle()
pawn_b.shape("./pieces/pawn-b.gif")
pawn_b.penup()


def drag_handler(x, y, name):
    name.goto(x, y)
    t.update()


t.hideturtle()
pawn_w.ondrag(lambda x, y: drag_handler(x, y, pawn_w))
pawn_b.ondrag(lambda x, y: drag_handler(x, y, pawn_b))
rook_w.ondrag(lambda x, y: drag_handler(x, y, rook_w))
rook_b.ondrag(lambda x, y: drag_handler(x, y, rook_b))
bishop_b.ondrag(lambda x, y: drag_handler(x, y, bishop_b))
bishop_w.ondrag(lambda x, y: drag_handler(x, y, bishop_w))
knight_w.ondrag(lambda x, y: drag_handler(x, y, knight_w))
knight_b.ondrag(lambda x, y: drag_handler(x, y, knight_b))
king_b.ondrag(lambda x, y: drag_handler(x, y, king_b))
king_w.ondrag(lambda x, y: drag_handler(x, y, king_w))
queen_b.ondrag(lambda x, y: drag_handler(x, y, queen_b))
queen_w.ondrag(lambda x, y: drag_handler(x, y, queen_w))
t.update()
t.done()
