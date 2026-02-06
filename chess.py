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
            board.fillcolor("lightgreen")
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


boardbox = {
    "a1": {"occupied": False, "cordinates": [-350, -350]},
    "b1": {"occupied": False, "cordinates": [-250, -350]},
    "c1": {"occupied": False, "cordinates": [-150, -350]},
    "d1": {"occupied": False, "cordinates": [-50, -350]},
    "e1": {"occupied": False, "cordinates": [50, -350]},
    "f1": {"occupied": False, "cordinates": [150, -350]},
    "g1": {"occupied": False, "cordinates": [250, -350]},
    "h1": {"occupied": False, "cordinates": [350, -350]},
    "a2": {"occupied": False, "cordinates": [-350, -250]},
    "b2": {"occupied": False, "cordinates": [-250, -250]},
    "c2": {"occupied": False, "cordinates": [-150, -250]},
    "d2": {"occupied": False, "cordinates": [-50, -250]},
    "e2": {"occupied": False, "cordinates": [50, -250]},
    "f2": {"occupied": False, "cordinates": [150, -250]},
    "g2": {"occupied": False, "cordinates": [250, -250]},
    "h2": {"occupied": False, "cordinates": [350, -250]},
    "a3": {"occupied": False, "cordinates": [-350, -150]},
    "b3": {"occupied": False, "cordinates": [-250, -150]},
    "c3": {"occupied": False, "cordinates": [-150, -150]},
    "d3": {"occupied": False, "cordinates": [-50, -150]},
    "e3": {"occupied": False, "cordinates": [50, -150]},
    "f3": {"occupied": False, "cordinates": [150, -150]},
    "g3": {"occupied": False, "cordinates": [250, -150]},
    "h3": {"occupied": False, "cordinates": [350, -150]},
    "a4": {"occupied": False, "cordinates": [-350, -50]},
    "b4": {"occupied": False, "cordinates": [-250, -50]},
    "c4": {"occupied": False, "cordinates": [-150, -50]},
    "d4": {"occupied": False, "cordinates": [-50, -50]},
    "e4": {"occupied": False, "cordinates": [50, -50]},
    "f4": {"occupied": False, "cordinates": [150, -50]},
    "g4": {"occupied": False, "cordinates": [250, -50]},
    "h4": {"occupied": False, "cordinates": [350, -50]},
    "a5": {"occupied": False, "cordinates": [-350, 50]},
    "b5": {"occupied": False, "cordinates": [-250, 50]},
    "c5": {"occupied": False, "cordinates": [-150, 50]},
    "d5": {"occupied": False, "cordinates": [-50, 50]},
    "e5": {"occupied": False, "cordinates": [50, 50]},
    "f5": {"occupied": False, "cordinates": [150, 50]},
    "g5": {"occupied": False, "cordinates": [250, 50]},
    "h5": {"occupied": False, "cordinates": [350, 50]},
    "a6": {"occupied": False, "cordinates": [-350, 150]},
    "b6": {"occupied": False, "cordinates": [-250, 150]},
    "c6": {"occupied": False, "cordinates": [-150, 150]},
    "d6": {"occupied": False, "cordinates": [-50, 150]},
    "e6": {"occupied": False, "cordinates": [50, 150]},
    "f6": {"occupied": False, "cordinates": [150, 150]},
    "g6": {"occupied": False, "cordinates": [250, 150]},
    "h6": {"occupied": False, "cordinates": [350, 150]},
    "a7": {"occupied": False, "cordinates": [-350, 250]},
    "b7": {"occupied": False, "cordinates": [-250, 250]},
    "c7": {"occupied": False, "cordinates": [-150, 250]},
    "d7": {"occupied": False, "cordinates": [-50, 250]},
    "e7": {"occupied": False, "cordinates": [50, 250]},
    "f7": {"occupied": False, "cordinates": [150, 250]},
    "g7": {"occupied": False, "cordinates": [250, 250]},
    "h7": {"occupied": False, "cordinates": [350, 250]},
    "a8": {"occupied": False, "cordinates": [-350, 350]},
    "b8": {"occupied": False, "cordinates": [-250, 350]},
    "c8": {"occupied": False, "cordinates": [-150, 350]},
    "d8": {"occupied": False, "cordinates": [-50, 350]},
    "e8": {"occupied": False, "cordinates": [50, 350]},
    "f8": {"occupied": False, "cordinates": [150, 350]},
    "g8": {"occupied": False, "cordinates": [250, 350]},
    "h8": {"occupied": False, "cordinates": [350, 350]},
}


rook_w_1 = t.Turtle()
rook_w_1.shape("./pieces/rook-w.gif")
rook_w_1.penup()

rook_w_2 = t.Turtle()
rook_w_2.shape("./pieces/rook-w.gif")
rook_w_2.penup()

rook_b_1 = t.Turtle()
rook_b_1.shape("./pieces/rook-b.gif")
rook_b_1.penup()

rook_b_2 = t.Turtle()
rook_b_2.shape("./pieces/rook-b.gif")
rook_b_2.penup()


bishop_w_1 = t.Turtle()
bishop_w_1.shape("./pieces/bishop-w.gif")
bishop_w_1.penup()

bishop_w_2 = t.Turtle()
bishop_w_2.shape("./pieces/bishop-w.gif")
bishop_w_2.penup()

bishop_b_1 = t.Turtle()
bishop_b_1.shape("./pieces/bishop-b.gif")
bishop_b_1.penup()

bishop_b_2 = t.Turtle()
bishop_b_2.shape("./pieces/bishop-b.gif")
bishop_b_2.penup()

knight_b_1 = t.Turtle()
knight_b_1.shape("./pieces/knight-b.gif")
knight_b_1.penup()

knight_b_2 = t.Turtle()
knight_b_2.shape("./pieces/knight-b.gif")
knight_b_2.penup()

knight_w_1 = t.Turtle()
knight_w_1.shape("./pieces/knight-w.gif")
knight_w_1.penup()

knight_w_2 = t.Turtle()
knight_w_2.shape("./pieces/knight-w.gif")
knight_w_2.penup()

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

pawn_w_1 = t.Turtle()
pawn_w_1.shape("./pieces/pawn-w.gif")
pawn_w_1.penup()

pawn_w_2 = t.Turtle()
pawn_w_2.shape("./pieces/pawn-w.gif")
pawn_w_2.penup()


pawn_w_3 = t.Turtle()
pawn_w_3.shape("./pieces/pawn-w.gif")
pawn_w_3.penup()

pawn_w_4 = t.Turtle()
pawn_w_4.shape("./pieces/pawn-w.gif")
pawn_w_4.penup()

pawn_w_5 = t.Turtle()
pawn_w_5.shape("./pieces/pawn-w.gif")
pawn_w_5.penup()

pawn_w_6 = t.Turtle()
pawn_w_6.shape("./pieces/pawn-w.gif")
pawn_w_6.penup()

pawn_w_7 = t.Turtle()
pawn_w_7.shape("./pieces/pawn-w.gif")
pawn_w_7.penup()

pawn_w_8 = t.Turtle()
pawn_w_8.shape("./pieces/pawn-w.gif")
pawn_w_8.penup()

pawn_b_1 = t.Turtle()
pawn_b_1.shape("./pieces/pawn-b.gif")
pawn_b_1.penup()

pawn_b_2 = t.Turtle()
pawn_b_2.shape("./pieces/pawn-b.gif")
pawn_b_2.penup()

pawn_b_3 = t.Turtle()
pawn_b_3.shape("./pieces/pawn-b.gif")
pawn_b_3.penup()

pawn_b_4 = t.Turtle()
pawn_b_4.shape("./pieces/pawn-b.gif")
pawn_b_4.penup()

pawn_b_5 = t.Turtle()
pawn_b_5.shape("./pieces/pawn-b.gif")
pawn_b_5.penup()

pawn_b_6 = t.Turtle()
pawn_b_6.shape("./pieces/pawn-b.gif")
pawn_b_6.penup()

pawn_b_7 = t.Turtle()
pawn_b_7.shape("./pieces/pawn-b.gif")
pawn_b_7.penup()

pawn_b_8 = t.Turtle()
pawn_b_8.shape("./pieces/pawn-b.gif")
pawn_b_8.penup()


def drag_handler(x, y, name):
    name.goto(x, y)
    t.update()


rook_w_1.penup()
rook_w_1.goto(-150, -150)
t.hideturtle()

pawn_w_1.ondrag(lambda x, y: drag_handler(x, y, pawn_w_1))
pawn_w_2.ondrag(lambda x, y: drag_handler(x, y, pawn_w_2))
pawn_w_3.ondrag(lambda x, y: drag_handler(x, y, pawn_w_3))
pawn_w_4.ondrag(lambda x, y: drag_handler(x, y, pawn_w_4))
pawn_w_5.ondrag(lambda x, y: drag_handler(x, y, pawn_w_5))
pawn_w_6.ondrag(lambda x, y: drag_handler(x, y, pawn_w_6))
pawn_w_7.ondrag(lambda x, y: drag_handler(x, y, pawn_w_7))
pawn_w_8.ondrag(lambda x, y: drag_handler(x, y, pawn_w_8))


pawn_b_1.ondrag(lambda x, y: drag_handler(x, y, pawn_b_1))
pawn_b_2.ondrag(lambda x, y: drag_handler(x, y, pawn_b_2))
pawn_b_3.ondrag(lambda x, y: drag_handler(x, y, pawn_b_3))
pawn_b_4.ondrag(lambda x, y: drag_handler(x, y, pawn_b_4))
pawn_b_5.ondrag(lambda x, y: drag_handler(x, y, pawn_b_5))
pawn_b_6.ondrag(lambda x, y: drag_handler(x, y, pawn_b_6))
pawn_b_7.ondrag(lambda x, y: drag_handler(x, y, pawn_b_7))
pawn_b_8.ondrag(lambda x, y: drag_handler(x, y, pawn_b_8))

rook_w_1.ondrag(lambda x, y: drag_handler(x, y, rook_w_1))
rook_w_2.ondrag(lambda x, y: drag_handler(x, y, rook_w_2))

rook_b_1.ondrag(lambda x, y: drag_handler(x, y, rook_b_1))
rook_b_2.ondrag(lambda x, y: drag_handler(x, y, rook_b_2))

bishop_b_1.ondrag(lambda x, y: drag_handler(x, y, bishop_b_1))
bishop_b_2.ondrag(lambda x, y: drag_handler(x, y, bishop_b_2))

bishop_w_1.ondrag(lambda x, y: drag_handler(x, y, bishop_w_1))
bishop_w_2.ondrag(lambda x, y: drag_handler(x, y, bishop_w_2))

knight_w_1.ondrag(lambda x, y: drag_handler(x, y, knight_w_1))
knight_w_2.ondrag(lambda x, y: drag_handler(x, y, knight_w_2))

knight_b_1.ondrag(lambda x, y: drag_handler(x, y, knight_b_1))
knight_b_2.ondrag(lambda x, y: drag_handler(x, y, knight_b_2))

king_b.ondrag(lambda x, y: drag_handler(x, y, king_b))
king_w.ondrag(lambda x, y: drag_handler(x, y, king_w))

queen_b.ondrag(lambda x, y: drag_handler(x, y, queen_b))
queen_w.ondrag(lambda x, y: drag_handler(x, y, queen_w))

columns = ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"]
pawns_b = [
    pawn_b_1,
    pawn_b_2,
    pawn_b_3,
    pawn_b_4,
    pawn_b_5,
    pawn_b_6,
    pawn_b_7,
    pawn_b_8,
]
for x in range(8):
    pawns_b[x].penup()
    pawns_b[x].goto(
        boardbox[columns[x]]["cordinates"][0], boardbox[columns[x]]["cordinates"][1]
    )


columns = ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"]
pawns_w = [
    pawn_w_1,
    pawn_w_2,
    pawn_w_3,
    pawn_w_4,
    pawn_w_5,
    pawn_w_6,
    pawn_w_7,
    pawn_w_8,
]
for x in range(8):
    pawns_w[x].penup()
    pawns_w[x].goto(
        boardbox[columns[x]]["cordinates"][0], boardbox[columns[x]]["cordinates"][1]
    )
rook_w_1.penup()
rook_w_1.goto(boardbox["a8"]["cordinates"][0], boardbox["a8"]["cordinates"][1])

rook_w_2.penup()
rook_w_2.goto(boardbox["h8"]["cordinates"][0], boardbox["a8"]["cordinates"][1])

rook_b_1.penup()
rook_b_1.goto(boardbox["a1"]["cordinates"][0], boardbox["a1"]["cordinates"][1])

rook_b_2.penup()
rook_b_2.goto(boardbox["h1"]["cordinates"][0], boardbox["a1"]["cordinates"][1])

knight_w_1.penup()
knight_w_1.goto(boardbox["b8"]["cordinates"][0], boardbox["b8"]["cordinates"][1])

knight_w_2.penup()
knight_w_2.goto(boardbox["g8"]["cordinates"][0], boardbox["g8"]["cordinates"][1])

knight_b_1.penup()
knight_b_1.goto(boardbox["b1"]["cordinates"][0], boardbox["b1"]["cordinates"][1])

knight_b_2.penup()
knight_b_2.goto(boardbox["g1"]["cordinates"][0], boardbox["g1"]["cordinates"][1])

bishop_w_1.penup()
bishop_w_1.goto(boardbox["c8"]["cordinates"][0], boardbox["c8"]["cordinates"][1])

bishop_w_2.penup()
bishop_w_2.goto(boardbox["f8"]["cordinates"][0], boardbox["f8"]["cordinates"][1])

bishop_b_1.penup()
bishop_b_1.goto(boardbox["c1"]["cordinates"][0], boardbox["c1"]["cordinates"][1])

bishop_b_2.penup()
bishop_b_2.goto(boardbox["f1"]["cordinates"][0], boardbox["f1"]["cordinates"][1])

king_w.penup()
king_w.goto(boardbox["e8"]["cordinates"][0], boardbox["e8"]["cordinates"][1])

king_b.penup()
king_b.goto(boardbox["e1"]["cordinates"][0], boardbox["e1"]["cordinates"][1])

queen_w.penup()
queen_w.goto(boardbox["d8"]["cordinates"][0], boardbox["d8"]["cordinates"][1])

queen_b.penup()
queen_b.goto(boardbox["d1"]["cordinates"][0], boardbox["d1"]["cordinates"][1])

t.update()
t.done()
