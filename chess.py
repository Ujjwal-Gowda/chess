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

pieces = []

FILES = "abcdefgh"
RANKS = "12345678"


class Piece:
    def __init__(self, kind, color, position, turtle):
        self.kind = kind
        self.color = color
        self.position = position
        self.turtle = turtle


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


def square_to_xy(file, rank):
    x = -350 + FILES.index(file) * 100
    y = -350 + (int(rank) - 1) * 100
    return x, y


def create_pawns(color, rank, image):
    pawns = []
    for file in FILES:
        turt = t.Turtle()
        turt.shape(image)
        turt.penup()
        square = f"{file}{rank}"
        print(square)
        x, y = square_to_xy(file, rank)
        turt.goto(x, y)
        pawn = Piece("pawn", color, square, turt)
        pawns.append(pawn)
    return pawns


white_pawns = create_pawns("white", 7, "./pieces/pawn-w.gif")
black_pawns = create_pawns("black", 2, "./pieces/pawn-b.gif")

pieces.extend(white_pawns)
pieces.extend(black_pawns)


def create_rooks(color, rank, image):
    rooks = []
    for file in ["a", "h"]:
        turt = t.Turtle()
        turt.shape(image)
        turt.penup()
        square = f"{file}{rank}"
        x, y = square_to_xy(file, rank)
        turt.goto(x, y)
        rook = Piece("rook", color, square, turt)
        rooks.append(rook)
    return rooks


white_rooks = create_rooks("white", 8, "./pieces/rook-w.gif")
black_rooks = create_rooks("black", 1, "./pieces/rook-b.gif")

pieces.extend(white_rooks)
pieces.extend(black_rooks)


def create_knight(color, rank, image):
    knights = []
    for file in ["b", "g"]:
        turt = t.Turtle()
        turt.shape(image)
        turt.penup()
        square = f"{file}{rank}"
        x, y = square_to_xy(file, rank)
        turt.goto(x, y)
        knight = Piece("knight", color, square, turt)
        knights.append(knight)
    return knights


white_knights = create_knight("white", 8, "./pieces/knight-w.gif")
black_knights = create_knight("black", 1, "./pieces/knight-b.gif")

pieces.extend(white_knights)
pieces.extend(black_knights)


def create_bishop(color, rank, image):
    bishops = []
    for file in ["c", "f"]:
        turt = t.Turtle()
        turt.shape(image)
        turt.penup()
        square = f"{file}{rank}"
        x, y = square_to_xy(file, rank)
        turt.goto(x, y)
        bishop = Piece("bishop", color, square, turt)
        bishops.append(bishop)
    return bishops


white_bishop = create_bishop("white", 8, "./pieces/bishop-w.gif")
black_bishop = create_bishop("black", 1, "./pieces/bishop-b.gif")

pieces.extend(white_bishop)
pieces.extend(black_bishop)


def create_king(color, rank, image):
    turt = t.Turtle()
    turt.shape(image)
    turt.penup()
    square = f"e{rank}"
    x, y = square_to_xy("e", rank)
    turt.goto(x, y)
    king = Piece("king", color, square, turt)
    return king


white_king = create_king("white", 8, "./pieces/king-w.gif")
black_king = create_king("black", 1, "./pieces/king-b.gif")

pieces.append(white_king)
pieces.append(black_king)


def create_queen(color, rank, image):
    turt = t.Turtle()
    turt.shape(image)
    turt.penup()
    square = f"d{rank}"
    x, y = square_to_xy("d", rank)
    turt.goto(x, y)
    queen = Piece("queen", color, square, turt)
    return queen


white_queen = create_queen("white", 8, "./pieces/queen-w.gif")
black_queen = create_queen("black", 1, "./pieces/queen-b.gif")

pieces.append(white_queen)
pieces.append(black_queen)
print("pieces", pieces)
boards = {}


for file in FILES:
    for rank in RANKS:
        boards[f"{file}{rank}"] = None

for piece in pieces:
    boards[piece.position] = piece

print("board", boards)


def xy_to_board(x, y):
    print(round(x + 350) / 100)
    file = FILES[round((x + 350) / 100)]
    rank = str(round((y + 350) / 100) + 1)
    return file + rank


selected_piece = None


def fxn(x, y):
    global selected_piece
    if selected_piece is None:
        t.goto(x, y)
        box = xy_to_board(x, y)
        if boards[box] is None:
            print("no piece selected")
        else:
            selected_piece = boards[box]
            print(box, selected_piece.kind, selected_piece.color)
        print(selected_piece)
    else:
        box = xy_to_board(x, y)
        # if is_legal_move(selected_piece, square):
        #     move_piece(selected_piece, square)
        if boards[box] is not None:
            return print("illegal move")
        move_piece(selected_piece, box)
        selected_piece = None


def move_piece(piece, box):
    piece.turtle.penup()
    boards[piece.position] = None
    piece.position = box
    x, y = square_to_xy(box[0], box[1])
    piece.turtle.goto(x, y)
    boards[box] = piece
    print("moving")
    t.update()


t.penup()
t.hideturtle()
window.onclick(fxn)
t.update()
t.done()
# boardbox = {
#     "a1": {"occupied": False, "cordinates": [-350, -350]},
#     "b1": {"occupied": False, "cordinates": [-250, -350]},
#     "c1": {"occupied": False, "cordinates": [-150, -350]},
#     "d1": {"occupied": False, "cordinates": [-50, -350]},
#     "e1": {"occupied": False, "cordinates": [50, -350]},
#     "f1": {"occupied": False, "cordinates": [150, -350]},
#     "g1": {"occupied": False, "cordinates": [250, -350]},
#     "h1": {"occupied": False, "cordinates": [350, -350]},
#     "a2": {"occupied": False, "cordinates": [-350, -250]},
#     "b2": {"occupied": False, "cordinates": [-250, -250]},
#     "c2": {"occupied": False, "cordinates": [-150, -250]},
#     "d2": {"occupied": False, "cordinates": [-50, -250]},
#     "e2": {"occupied": False, "cordinates": [50, -250]},
#     "f2": {"occupied": False, "cordinates": [150, -250]},
#     "g2": {"occupied": False, "cordinates": [250, -250]},
#     "h2": {"occupied": False, "cordinates": [350, -250]},
#     "a3": {"occupied": False, "cordinates": [-350, -150]},
#     "b3": {"occupied": False, "cordinates": [-250, -150]},
#     "c3": {"occupied": False, "cordinates": [-150, -150]},
#     "d3": {"occupied": False, "cordinates": [-50, -150]},
#     "e3": {"occupied": False, "cordinates": [50, -150]},
#     "f3": {"occupied": False, "cordinates": [150, -150]},
#     "g3": {"occupied": False, "cordinates": [250, -150]},
#     "h3": {"occupied": False, "cordinates": [350, -150]},
#     "a4": {"occupied": False, "cordinates": [-350, -50]},
#     "b4": {"occupied": False, "cordinates": [-250, -50]},
#     "c4": {"occupied": False, "cordinates": [-150, -50]},
#     "d4": {"occupied": False, "cordinates": [-50, -50]},
#     "e4": {"occupied": False, "cordinates": [50, -50]},
#     "f4": {"occupied": False, "cordinates": [150, -50]},
#     "g4": {"occupied": False, "cordinates": [250, -50]},
#     "h4": {"occupied": False, "cordinates": [350, -50]},
#     "a5": {"occupied": False, "cordinates": [-350, 50]},
#     "b5": {"occupied": False, "cordinates": [-250, 50]},
#     "c5": {"occupied": False, "cordinates": [-150, 50]},
#     "d5": {"occupied": False, "cordinates": [-50, 50]},
#     "e5": {"occupied": False, "cordinates": [50, 50]},
#     "f5": {"occupied": False, "cordinates": [150, 50]},
#     "g5": {"occupied": False, "cordinates": [250, 50]},
#     "h5": {"occupied": False, "cordinates": [350, 50]},
#     "a6": {"occupied": False, "cordinates": [-350, 150]},
#     "b6": {"occupied": False, "cordinates": [-250, 150]},
#     "c6": {"occupied": False, "cordinates": [-150, 150]},
#     "d6": {"occupied": False, "cordinates": [-50, 150]},
#     "e6": {"occupied": False, "cordinates": [50, 150]},
#     "f6": {"occupied": False, "cordinates": [150, 150]},
#     "g6": {"occupied": False, "cordinates": [250, 150]},
#     "h6": {"occupied": False, "cordinates": [350, 150]},
#     "a7": {"occupied": False, "cordinates": [-350, 250]},
#     "b7": {"occupied": False, "cordinates": [-250, 250]},
#     "c7": {"occupied": False, "cordinates": [-150, 250]},
#     "d7": {"occupied": False, "cordinates": [-50, 250]},
#     "e7": {"occupied": False, "cordinates": [50, 250]},
#     "f7": {"occupied": False, "cordinates": [150, 250]},
#     "g7": {"occupied": False, "cordinates": [250, 250]},
#     "h7": {"occupied": False, "cordinates": [350, 250]},
#     "a8": {"occupied": False, "cordinates": [-350, 350]},
#     "b8": {"occupied": False, "cordinates": [-250, 350]},
#     "c8": {"occupied": False, "cordinates": [-150, 350]},
#     "d8": {"occupied": False, "cordinates": [-50, 350]},
#     "e8": {"occupied": False, "cordinates": [50, 350]},
#     "f8": {"occupied": False, "cordinates": [150, 350]},
#     "g8": {"occupied": False, "cordinates": [250, 350]},
#     "h8": {"occupied": False, "cordinates": [350, 350]},
# }


# rook_w_1 = t.Turtle()
# rook_w_1.shape("./pieces/rook-w.gif")
# rook_w_1.penup()
#
# rook_w_2 = t.Turtle()
# rook_w_2.shape("./pieces/rook-w.gif")
# rook_w_2.penup()
#
# rook_b_1 = t.Turtle()
# rook_b_1.shape("./pieces/rook-b.gif")
# rook_b_1.penup()
#
# rook_b_2 = t.Turtle()
# rook_b_2.shape("./pieces/rook-b.gif")
# rook_b_2.penup()
#
#
# bishop_w_1 = t.Turtle()
# bishop_w_1.shape("./pieces/bishop-w.gif")
# bishop_w_1.penup()
#
# bishop_w_2 = t.Turtle()
# bishop_w_2.shape("./pieces/bishop-w.gif")
# bishop_w_2.penup()
#
# bishop_b_1 = t.Turtle()
# bishop_b_1.shape("./pieces/bishop-b.gif")
# bishop_b_1.penup()
#
# bishop_b_2 = t.Turtle()
# bishop_b_2.shape("./pieces/bishop-b.gif")
# bishop_b_2.penup()
#
# knight_b_1 = t.Turtle()
# knight_b_1.shape("./pieces/knight-b.gif")
# knight_b_1.penup()
#
# knight_b_2 = t.Turtle()
# knight_b_2.shape("./pieces/knight-b.gif")
# knight_b_2.penup()
#
# knight_w_1 = t.Turtle()
# knight_w_1.shape("./pieces/knight-w.gif")
# knight_w_1.penup()
#
# knight_w_2 = t.Turtle()
# knight_w_2.shape("./pieces/knight-w.gif")
# knight_w_2.penup()
#
# king_w = t.Turtle()
# king_w.shape("./pieces/king-w.gif")
# king_w.penup()
#
# king_b = t.Turtle()
# king_b.shape("./pieces/king-b.gif")
# king_b.penup()
#
# queen_b = t.Turtle()
# queen_b.shape("./pieces/queen-b.gif")
# queen_b.penup()
#
# queen_w = t.Turtle()
# queen_w.shape("./pieces/queen-w.gif")
# queen_w.penup()
#
# pawn_w_1 = t.Turtle()
# pawn_w_1.shape("./pieces/pawn-w.gif")
# pawn_w_1.penup()
#
# pawn_w_2 = t.Turtle()
# pawn_w_2.shape("./pieces/pawn-w.gif")
# pawn_w_2.penup()
#
#
# pawn_w_3 = t.Turtle()
# pawn_w_3.shape("./pieces/pawn-w.gif")
# pawn_w_3.penup()
#
# pawn_w_4 = t.Turtle()
# pawn_w_4.shape("./pieces/pawn-w.gif")
# pawn_w_4.penup()
#
# pawn_w_5 = t.Turtle()
# pawn_w_5.shape("./pieces/pawn-w.gif")
# pawn_w_5.penup()
#
# pawn_w_6 = t.Turtle()
# pawn_w_6.shape("./pieces/pawn-w.gif")
# pawn_w_6.penup()
#
# pawn_w_7 = t.Turtle()
# pawn_w_7.shape("./pieces/pawn-w.gif")
# pawn_w_7.penup()
#
# pawn_w_8 = t.Turtle()
# pawn_w_8.shape("./pieces/pawn-w.gif")
# pawn_w_8.penup()
#
# pawn_b_1 = t.Turtle()
# pawn_b_1.shape("./pieces/pawn-b.gif")
# pawn_b_1.penup()
#
# pawn_b_2 = t.Turtle()
# pawn_b_2.shape("./pieces/pawn-b.gif")
# pawn_b_2.penup()
#
# pawn_b_3 = t.Turtle()
# pawn_b_3.shape("./pieces/pawn-b.gif")
# pawn_b_3.penup()
#
# pawn_b_4 = t.Turtle()
# pawn_b_4.shape("./pieces/pawn-b.gif")
# pawn_b_4.penup()
#
# pawn_b_5 = t.Turtle()
# pawn_b_5.shape("./pieces/pawn-b.gif")
# pawn_b_5.penup()
#
# pawn_b_6 = t.Turtle()
# pawn_b_6.shape("./pieces/pawn-b.gif")
# pawn_b_6.penup()
#
# pawn_b_7 = t.Turtle()
# pawn_b_7.shape("./pieces/pawn-b.gif")
# pawn_b_7.penup()
#
# pawn_b_8 = t.Turtle()
# pawn_b_8.shape("./pieces/pawn-b.gif")
# pawn_b_8.penup()
#


# boards = {}
# newx = 0
# newy = 0
#
#
# def drag_handler(x, y, name):
#     name.goto(x, y)
#     newx = round_to_nearest(x, 50)
#     newy = round_to_nearest(y, 50)
#     if (newx / 50) % 2 == 0:
#         newy += 50
#     print(newx, newy)
#     name.goto(newx, newy)
#     t.update()
#
#
# def round_to_nearest(n, base):
#     return round(n / base) * base
#
#
# pawn_w_1.ondrag(lambda x, y: drag_handler(x, y, pawn_w_1))
# pawn_w_2.ondrag(lambda x, y: drag_handler(x, y, pawn_w_2))
# pawn_w_3.ondrag(lambda x, y: drag_handler(x, y, pawn_w_3))
# pawn_w_4.ondrag(lambda x, y: drag_handler(x, y, pawn_w_4))
# pawn_w_5.ondrag(lambda x, y: drag_handler(x, y, pawn_w_5))
# pawn_w_6.ondrag(lambda x, y: drag_handler(x, y, pawn_w_6))
# pawn_w_7.ondrag(lambda x, y: drag_handler(x, y, pawn_w_7))
# pawn_w_8.ondrag(lambda x, y: drag_handler(x, y, pawn_w_8))
#
#
# pawn_b_1.ondrag(lambda x, y: drag_handler(x, y, pawn_b_1))
# pawn_b_2.ondrag(lambda x, y: drag_handler(x, y, pawn_b_2))
# pawn_b_3.ondrag(lambda x, y: drag_handler(x, y, pawn_b_3))
# pawn_b_4.ondrag(lambda x, y: drag_handler(x, y, pawn_b_4))
# pawn_b_5.ondrag(lambda x, y: drag_handler(x, y, pawn_b_5))
# pawn_b_6.ondrag(lambda x, y: drag_handler(x, y, pawn_b_6))
# pawn_b_7.ondrag(lambda x, y: drag_handler(x, y, pawn_b_7))
# pawn_b_8.ondrag(lambda x, y: drag_handler(x, y, pawn_b_8))
#
# rook_w_1.ondrag(lambda x, y: drag_handler(x, y, rook_w_1))
# rook_w_2.ondrag(lambda x, y: drag_handler(x, y, rook_w_2))
#
# rook_b_1.ondrag(lambda x, y: drag_handler(x, y, rook_b_1))
# rook_b_2.ondrag(lambda x, y: drag_handler(x, y, rook_b_2))
#
# bishop_b_1.ondrag(lambda x, y: drag_handler(x, y, bishop_b_1))
# bishop_b_2.ondrag(lambda x, y: drag_handler(x, y, bishop_b_2))
#
# bishop_w_1.ondrag(lambda x, y: drag_handler(x, y, bishop_w_1))
# bishop_w_2.ondrag(lambda x, y: drag_handler(x, y, bishop_w_2))
#
# knight_w_1.ondrag(lambda x, y: drag_handler(x, y, knight_w_1))
# knight_w_2.ondrag(lambda x, y: drag_handler(x, y, knight_w_2))
#
# knight_b_1.ondrag(lambda x, y: drag_handler(x, y, knight_b_1))
# knight_b_2.ondrag(lambda x, y: drag_handler(x, y, knight_b_2))
#
# king_b.ondrag(lambda x, y: drag_handler(x, y, king_b))
# king_w.ondrag(lambda x, y: drag_handler(x, y, king_w))
#
# queen_b.ondrag(lambda x, y: drag_handler(x, y, queen_b))
# queen_w.ondrag(lambda x, y: drag_handler(x, y, queen_w))
#

# columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
# pawns_b = [
#     pawn_b_1,
#     pawn_b_2,
#     pawn_b_3,
#     pawn_b_4,
#     pawn_b_5,
#     pawn_b_6,
#     pawn_b_7,
#     pawn_b_8,
# ]
# for x in range(8):
#     pawns_b[x].penup()
#     alph = columns[x]
#     a, n = square_to_xy(alph, 2)
#     pawns_b[x].goto(a, n)
#
#
# pawns_w = [
#     pawn_w_1,
#     pawn_w_2,
#     pawn_w_3,
#     pawn_w_4,
#     pawn_w_5,
#     pawn_w_6,
#     pawn_w_7,
#     pawn_w_8,
# ]
# for x in range(8):
#     pawns_w[x].penup()
#     alph = columns[x]
#     a, n = square_to_xy(alph, 7)
#     pawns_w[x].goto(a, n)
# rook_w_1.penup()
# a, n = square_to_xy("a", 8)
# rook_w_1.goto(a, n)
#
#
# rook_w_2.penup()
# a, n = square_to_xy("h", 8)
# rook_w_2.goto(a, n)
#
# rook_b_1.penup()
# a, n = square_to_xy("a", 1)
# rook_b_1.goto(a, n)
#
# rook_b_2.penup()
# a, n = square_to_xy("h", 1)
# rook_b_2.goto(a, n)
#
# knight_w_1.penup()
# a, n = square_to_xy("b", 8)
# knight_w_1.goto(a, n)
#
# knight_w_2.penup()
# a, n = square_to_xy("g", 8)
# knight_w_2.goto(a, n)
#
# knight_b_1.penup()
# a, n = square_to_xy("b", 1)
# knight_b_1.goto(a, n)
#
# knight_b_2.penup()
# a, n = square_to_xy("g", 1)
# knight_b_2.goto(a, n)
#
# bishop_w_1.penup()
# a, n = square_to_xy("c", 8)
# bishop_w_1.goto(a, n)
#
# bishop_w_2.penup()
# a, n = square_to_xy("f", 8)
# bishop_w_2.goto(a, n)
#
# bishop_b_1.penup()
# a, n = square_to_xy("c", 1)
# bishop_b_1.goto(a, n)
#
# bishop_b_2.penup()
# a, n = square_to_xy("f", 1)
# bishop_b_2.goto(a, n)
#
# king_w.penup()
# a, n = square_to_xy("e", 8)
# king_w.goto(a, n)
#
# king_b.penup()
# a, n = square_to_xy("e", 1)
# king_b.goto(a, n)
#
# queen_w.penup()
# a, n = square_to_xy("d", 8)
# queen_w.goto(a, n)
#
# queen_b.penup()
# a, n = square_to_xy("d", 1)
# queen_b.goto(a, n)
#
