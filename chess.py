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
current_turn = ["white", "black"]
FILES = "abcdefgh"
RANKS = "12345678"
black_rm = []
white_rm = []


class Piece:
    def __init__(self, kind, color, position, turtle, move_count):
        self.kind = kind
        self.color = color
        self.position = position
        self.turtle = turtle
        self.move_count = move_count


class Move:
    def __init__(self, piece, from_sq, to_sq, captured, prev_move_count):
        self.piece = piece
        self.from_sq = from_sq
        self.to_sq = to_sq
        self.captured = captured
        self.prev_move_count = prev_move_count


for boxes in range(8):
    for box in range(8):
        if (boxes + box) % 2 == 0:
            board.fillcolor("lightblue")
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
        pawn = Piece("pawn", color, square, turt, move_count=0)
        pawns.append(pawn)
    return pawns


white_pawns = create_pawns("white", 2, "./pieces/pawn-w.gif")
black_pawns = create_pawns("black", 7, "./pieces/pawn-b.gif")

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
        rook = Piece("rook", color, square, turt, move_count=0)
        rooks.append(rook)
    return rooks


white_rooks = create_rooks("white", 1, "./pieces/rook-w.gif")
black_rooks = create_rooks("black", 8, "./pieces/rook-b.gif")

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
        knight = Piece("knight", color, square, turt, move_count=0)
        knights.append(knight)
    return knights


white_knights = create_knight("white", 1, "./pieces/knight-w.gif")
black_knights = create_knight("black", 8, "./pieces/knight-b.gif")

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
        bishop = Piece("bishop", color, square, turt, move_count=0)
        bishops.append(bishop)
    return bishops


white_bishop = create_bishop("white", 1, "./pieces/bishop-w.gif")
black_bishop = create_bishop("black", 8, "./pieces/bishop-b.gif")

pieces.extend(white_bishop)
pieces.extend(black_bishop)


def create_king(color, rank, image):
    turt = t.Turtle()
    turt.shape(image)
    turt.penup()
    square = f"e{rank}"
    x, y = square_to_xy("e", rank)
    turt.goto(x, y)
    king = Piece("king", color, square, turt, move_count=0)
    return king


white_king = create_king("white", 1, "./pieces/king-w.gif")
black_king = create_king("black", 8, "./pieces/king-b.gif")

pieces.append(white_king)
pieces.append(black_king)


def create_queen(color, rank, image):
    turt = t.Turtle()
    turt.shape(image)
    turt.penup()
    square = f"d{rank}"
    x, y = square_to_xy("d", rank)
    turt.goto(x, y)
    queen = Piece("queen", color, square, turt, move_count=0)
    return queen


white_queen = create_queen("white", 1, "./pieces/queen-w.gif")
black_queen = create_queen("black", 8, "./pieces/queen-b.gif")

pieces.append(white_queen)
pieces.append(black_queen)
boards = {}


for file in FILES:
    for rank in RANKS:
        boards[f"{file}{rank}"] = None

for piece in pieces:
    boards[piece.position] = piece


def xy_to_board(x, y):

    file_idx = int((x + 400) // 100)
    rank_idx = int((y + 400) // 100)
    print(file_idx, rank_idx)
    if not (0 <= file_idx < 8 and 0 <= rank_idx < 8):
        return None

    return FILES[file_idx] + RANKS[rank_idx]
    print(round(x + 350) / 100)
    file = FILES[round((x + 350) / 100)]
    rank = str(round((y + 350) / 100) + 1)
    return file + rank


selected_piece = None


ind = 0


def fxn(x, y):
    global selected_piece, ind
    if not (-400 < x < 400 and -400 < y < 400):
        return

    box = xy_to_board(x, y)
    if box is None:
        return

    clicked_piece = boards[box]

    if selected_piece is None:
        if clicked_piece is None:
            return
        if clicked_piece.color != current_turn[ind]:
            print(f"{current_turn[ind]} turn")
            return

        selected_piece = clicked_piece
        print("selected:", box)
        return
    # deselect
    if box == selected_piece.position:
        selected_piece = None
        print("deselected")
        return

    if clicked_piece and clicked_piece.color == selected_piece.color:
        selected_piece = clicked_piece
        print("switched selection to:", box)
        return

    if clicked_piece is None or boards[box].color != selected_piece.color:

        print("selected_piece")

        if is_legal_move(selected_piece, box):
            move_piece(selected_piece, box)
            selected_piece = None
            ind = 1 - ind
        return


def is_legal_move(piece, box):
    file_from = FILES.index(piece.position[0])
    rank_from = int(piece.position[1])

    file_to = FILES.index(box[0])
    rank_to = int(box[1])
    direction = 1 if piece.color == "white" else -1

    if piece.kind == "pawn":
        # same lane
        if file_from == file_to:
            if rank_from + direction == rank_to and boards[box] is None:
                return move_is_safe(piece, box)

            if piece.move_count == 0 and rank_from + 2 * direction == rank_to:
                intermediate_box = piece.position[0] + str(rank_from + direction)
                if boards[intermediate_box] is None and boards[box] is None:
                    return move_is_safe(piece, box)
        # capture
        if abs(file_from - file_to) == 1 and rank_from + direction == rank_to:
            if boards[box] and boards[box].color != piece.color:
                pie = boards[box]
                (
                    black_rm.append(pie)
                    if piece.color == "white"
                    else white_rm.append(pie)
                )
                print(white_rm, black_rm)
                return move_is_safe(piece, box)

        return False
    if piece.kind == "rook":
        # vertical movement
        if file_from == file_to:
            step = 1 if rank_to > rank_from else -1
            for r in range(rank_from + step, rank_to, step):
                square = piece.position[0] + str(r)
                if boards[square] is not None:
                    return False
        # horizontal movement
        elif rank_from == rank_to:
            step = 1 if file_to > file_from else -1
            for f in range(file_from + step, file_to, step):
                square = FILES[f] + piece.position[1]
                if boards[square] is not None:
                    return False
        else:
            return False

        if boards[box] is None:
            return move_is_safe(piece, box)

        if boards[box].color != piece.color:
            return move_is_safe(piece, box)

        return False

    if piece.kind == "bishop":
        df = file_to - file_from
        dr = rank_to - rank_from

        if abs(df) != abs(dr):
            return False

        step_file = 1 if df > 0 else -1
        step_rank = 1 if dr > 0 else -1
        f = file_from + step_file
        r = rank_from + step_rank

        while f != file_to and r != rank_to:
            square = FILES[f] + str(r)
            if boards[square] is not None:
                return False
            f += step_file
            r += step_rank
        if boards[box] is None:
            return move_is_safe(piece, box)

        if boards[box].color != piece.color:
            return move_is_safe(piece, box)

        return False

    if piece.kind == "queen":

        piece.kind = "rook"
        if is_legal_move(piece, box):
            piece.kind = "queen"
            return True

        piece.kind = "bishop"
        if is_legal_move(piece, box):
            piece.kind = "queen"
            return True

        piece.kind = "queen"
        return False

    if piece.kind == "knight":
        df = abs(file_from - file_to)
        dr = abs(rank_from - rank_to)

        if (df == 1 and dr == 2) or (df == 2 and dr == 1):
            if boards[box] is None:
                return move_is_safe(piece, box)
            if boards[box].color != piece.color:
                return move_is_safe(piece, box)
        return False

    if piece.kind == "king":
        df = file_to - file_from
        dr = rank_to - rank_from
        enemy = "white" if piece.color == "black" else "black"
        if max(abs(df), abs(dr)) == 1:
            if boards[box] and boards[box].color == piece.color:
                return False
            if is_square_attacked(box, enemy):
                return False
            return move_is_safe(piece, box)

        # Castling
        if piece.move_count != 0 or dr != 0:
            return False

        rank = "1" if piece.color == "white" else "8"

        # King side
        if df == 2:
            rook_square = "h" + rank
            path = ["f" + rank, "g" + rank]

        # Queen side
        elif df == -2:
            rook_square = "a" + rank
            path = ["d" + rank, "c" + rank]

        else:
            return False

        rook = boards.get(rook_square)
        if not rook or rook.kind != "rook" or rook.move_count != 0:
            return False

        if in_check(piece.color):
            return False

        for sq in path:
            if boards[sq] is not None:
                return False
            if is_square_attacked(sq, enemy):
                return False

        return True


def move_piece(piece, box):
    from_square = piece.position
    captured = boards[box]
    if captured:
        captured.turtle.shape("blank")
    # Castling
    if (
        piece.kind == "king"
        and abs(FILES.index(from_square[0]) - FILES.index(box[0])) == 2
    ):
        rank = from_square[1]

        if box[0] == "g":  # king side
            rook_from = "h" + rank
            rook_to = "f" + rank
        else:  # queen side
            rook_from = "a" + rank
            rook_to = "d" + rank

        rook = boards[rook_from]
        boards[rook_from] = None
        rook.position = rook_to
        x, y = square_to_xy(rook_to[0], rook_to[1])
        rook.turtle.goto(x, y)
        boards[rook_to] = rook
        rook.move_count += 1

    boards[piece.position] = None
    piece.position = box
    x, y = square_to_xy(box[0], box[1])
    piece.turtle.goto(x, y)
    boards[box] = piece
    piece.move_count += 1
    pawn_promotion()
    generate_moves("black")

    print("moving")
    if in_check("black"):
        print("black in check")
    if in_check("white"):
        print("white in check")

    if is_checkmate("black"):
        print("checkmate")
    if is_checkmate("white"):
        print("checkmate")

    if is_stalemate("black"):
        print("stalemate")
    if is_stalemate("white"):
        print("stalemate")
    t.update()


def is_square_attacked(square, by_color):
    file = FILES.index(square[0])
    rank = int(square[1])

    pawn_dir = 1 if by_color == "white" else -1
    for df in (-1, 1):
        f = file + df
        r = rank - pawn_dir
        if 0 <= f < 8 and 1 <= r <= 8:
            p = boards[FILES[f] + str(r)]
            if p and p.color == by_color and p.kind == "pawn":
                return True

    knight_moves = [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
    ]
    for df, dr in knight_moves:
        f = file + df
        r = rank + dr
        if 0 <= f < 8 and 1 <= r <= 8:
            p = boards[FILES[f] + str(r)]
            if p and p.color == by_color and p.kind == "knight":
                return True

    for df, dr in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        f = file + df
        r = rank + dr
        while 0 <= f < 8 and 1 <= r <= 8:
            p = boards[FILES[f] + str(r)]
            if p:
                if p.color == by_color and p.kind in ("bishop", "queen"):
                    return True
                break
            f += df
            r += dr

    for df, dr in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        f = file + df
        r = rank + dr
        while 0 <= f < 8 and 1 <= r <= 8:
            p = boards[FILES[f] + str(r)]
            if p:
                if p.color == by_color and p.kind in ("rook", "queen"):
                    return True
                break
            f += df
            r += dr

    for df in (-1, 0, 1):
        for dr in (-1, 0, 1):
            if df == 0 and dr == 0:
                continue
            f = file + df
            r = rank + dr
            if 0 <= f < 8 and 1 <= r <= 8:
                p = boards[FILES[f] + str(r)]
                if p and p.color == by_color and p.kind == "king":
                    return True

    return False


def find_king(color):
    for box in boards:
        obj = boards[box]
        if obj is not None and obj.kind == "king" and obj.color == color:
            return box
    pass


def move_is_safe(piece, box):
    original_square = piece.position
    captured = boards[box]

    boards[original_square] = None
    boards[box] = piece
    piece.position = box

    illegal = in_check(piece.color)

    piece.position = original_square
    boards[original_square] = piece
    boards[box] = captured

    return not illegal


def in_check(color):
    king_square = find_king(color)
    enemy = "white" if color == "black" else "black"
    return is_square_attacked(king_square, enemy)


def is_checkmate(color):
    if not in_check(color):
        return False

    for box in boards:
        piece = boards[box]
        if piece and piece.color == color:
            for f in FILES:
                for r in "12345678":
                    target = f + r
                    if is_legal_move(piece, target) and move_is_safe(piece, target):
                        return False
    return True


def is_stalemate(color):
    if in_check(color):
        return False

    for box in boards:
        piece = boards[box]
        if piece and piece.color == color:
            for f in FILES:
                for r in "12345678":
                    target = f + r
                    if is_legal_move(piece, target) and move_is_safe(piece, target):
                        return False
    return True


def pawn_promotion():
    for color in ["white", "black"]:
        rank = "8" if color == "white" else "1"
        for box in boards:
            piece = boards[box]
            if piece and piece.kind == "pawn" and piece.color == color:
                if box[1] == rank:
                    piece.kind = "queen"
                    piece.turtle.shape(
                        "./pieces/queen-w.gif"
                        if piece.color == "white"
                        else "./pieces/queen-b.gif"
                    )
    return


def generate_moves(color):
    moves = []
    for box in boards:
        piece = boards[box]
        if piece and piece.color == color:
            for f in FILES:
                for r in "12345678":
                    target = f + r
                    if is_legal_move(piece, target) and move_is_safe(piece, target):
                        moves.append((piece, target))
    print(moves[0], moves[1])
    return moves


def make_move(piece, to_sq):
    from_sq = piece.position
    captured = boards[to_sq]
    prev_move_count = piece.move_count

    move = Move(piece, from_sq, to_sq, captured, prev_move_count)

    boards[from_sq] = None
    piece.position = to_sq
    boards[to_sq] = piece
    piece.move_count += 1

    return move


def undo_move(move):
    piece = move.piece
    boards[move.to_sq] = move.captured
    if move.captured:
        move.captured.position = move.to_sq
    boards[move.from_sq] = piece
    piece.position = move.from_sq
    piece.move_count = move.prev_move_count


t.penup()
t.hideturtle()
window.onclick(fxn)
t.update()
t.done()
