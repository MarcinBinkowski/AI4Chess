class Chessboard:

    def __init__(self):
        self.chessboard = \
            [
                ["BP", "BJ", "BP", "BP", "BP", "BP", "BP", "BP"],
                ["BR", "BJ", "BB", "BQ", "BK", "BB", "BJ", "BR"],
                ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
                ["WR", "WJ", "WB", "WQ", "WK", "WB", "WJ", "WR"]
            ]

    def print_chessboard(self):
        for i in self.chessboard:
            print(i)


class Piece:

    def __init__(self, color, x, y, x_position, y_position):
        self.color = color
        self.x = x
        self.y = y
        self.x_position = x_position
        self.y_position = y_position
        self.all_possible_moves = []
        self.all_valid_possible_moves = []

    def __str__(self):
        pass

    def move(self, x, y):
        self.x = x
        self.y = y

    def get_all_moves(self):
        pass

    def remove_impossible_moves(self):
        for i in self.all_possible_moves[:]:
            if i[0] < 0 or i[0] > 7 or i[1] < 0 or i[1] > 7:
                self.all_possible_moves.remove(i)


class Pawn(Piece):

    def __init__(self, color, x, y, x_position, y_position, is_moved):
        super().__init__(color, x, y, x_position, y_position)
        self.is_moved = is_moved
        self.value = 1

    def __str__(self):
        return f"{self.color} Pawn"

    def get_all_moves(self):
        if self.color == "White":
            if not self.is_moved:
                self.all_possible_moves.append((self.x, self.y - 2))
            self.all_possible_moves.append((self.x, self.y - 1))
            self.all_possible_moves.append((self.x + 1, self.y - 1))
            self.all_possible_moves.append((self.x - 1, self.y - 1))
        else:
            if not self.is_moved:
                self.all_possible_moves.append((self.x, self.y + 2))
            self.all_possible_moves.append((self.x, self.y + 1))
            self.all_possible_moves.append((self.x + 1, self.y + 1))
            self.all_possible_moves.append((self.x - 1, self.y + 1))
        self.remove_impossible_moves()


class Rook(Piece):

    def __init__(self, color, x, y, x_position, y_position, ):
        super().__init__(color, x, y, x_position, y_position)
        self.value = 5

    def __str__(self):
        return f"{self.color} Rook"

    def get_all_moves(self):
        for i in range(1, 8):
            self.all_possible_moves.append((self.x-i, self.y))
            self.all_possible_moves.append((self.x+i, self.y))
            self.all_possible_moves.append((self.x, self.y-i))
            self.all_possible_moves.append((self.x, self.y+i))
        self.remove_impossible_moves()


class Jumper(Piece):

    def __init__(self, color, x, y, x_position, y_position, ):
        super().__init__(color, x, y, x_position, y_position)
        self.value = 3

    def __str__(self):
        return f"{self.color} Rook"

    def get_all_moves(self):
        self.all_possible_moves.append((self.x + 1, self.y + 2))
        self.all_possible_moves.append((self.x + 1, self.y - 2))
        self.all_possible_moves.append((self.x + 2, self.y + 1))
        self.all_possible_moves.append((self.x + 2, self.y - 1))
        self.all_possible_moves.append((self.x - 1, self.y + 2))
        self.all_possible_moves.append((self.x - 1, self.y - 2))
        self.all_possible_moves.append((self.x - 2, self.y + 1))
        self.all_possible_moves.append((self.x - 2, self.y - 1))

        self.remove_impossible_moves()


class Bishop(Piece):

    def __init__(self, color, x, y, x_position, y_position, ):
        super().__init__(color, x, y, x_position, y_position)
        self.value = 3

    def __str__(self):
        return f"{self.color} Rook"

    def get_all_moves(self):
        for i in range(1, 8):
            self.all_possible_moves.append((self.x + i, self.y + i))
            self.all_possible_moves.append((self.x + i, self.y - i))
            self.all_possible_moves.append((self.x - i, self.y + i))
            self.all_possible_moves.append((self.x - i, self.y - i))

        self.remove_impossible_moves()


class Queen(Piece):

    def __init__(self, color, x, y, x_position, y_position, ):
        super().__init__(color, x, y, x_position, y_position)
        self.value = 9

    def __str__(self):
        return f"{self.color} Rook"

    def get_all_moves(self):
        for i in range(1, 8):
            self.all_possible_moves.append((self.x + i, self.y + i))
            self.all_possible_moves.append((self.x + i, self.y - i))
            self.all_possible_moves.append((self.x - i, self.y + i))
            self.all_possible_moves.append((self.x - i, self.y - i))
            self.all_possible_moves.append((self.x - i, self.y))
            self.all_possible_moves.append((self.x + i, self.y))
            self.all_possible_moves.append((self.x, self.y - i))
            self.all_possible_moves.append((self.x, self.y + i))

        self.remove_impossible_moves()


class King(Piece):

    def __str__(self):
        return f"{self.color} Rook"

    def get_all_moves(self):
        self.all_possible_moves.append((self.x, self.y - 1))
        self.all_possible_moves.append((self.x, self.y + 1))
        self.all_possible_moves.append((self.x - 1, self.y))
        self.all_possible_moves.append((self.x + 1, self.y))
        self.all_possible_moves.append((self.x + 1, self.y - 1))
        self.all_possible_moves.append((self.x - 1, self.y - 1))
        self.all_possible_moves.append((self.x + 1, self.y + 1))
        self.all_possible_moves.append((self.x - 1, self.y + 1))

        self.remove_impossible_moves()





a = Pawn("White", 1,2, 0, 0, False)
a.get_all_moves()
print(a.all_possible_moves)
rook = Rook("White", 1, 2, 0, 0)
rook.get_all_moves()
print(rook.all_possible_moves)
jumper = Jumper("White", 4, 4, 0, 0)
jumper.get_all_moves()
print(jumper.all_possible_moves)
bishop = Bishop("White", 4, 4, 0, 0)
bishop.get_all_moves()
print(bishop.all_possible_moves)
king = King("White", 4, 4, 0, 0)
king.get_all_moves()
print(king.all_possible_moves)
queen = Queen("White", 4, 4, 0, 0)
queen.get_all_moves()
print(queen.all_possible_moves)
#chessboard = Chessboard()
#chessboard.print_chessboard()