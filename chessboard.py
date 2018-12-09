class Chessboard:

    def __init__(self):
        self.chessboard = [["  " for x in range(8)]for y in range(8)]

    def create_pawns(self):
        for i in range(8):
            self.chessboard[1][i] = Pawn("Black", i, 1, 0, 0)
            self.chessboard[6][i] = Pawn("White", i, 6, 0, 0)

    def create_rooks(self):
        self.chessboard[0][0] = Rook("Black", 0, 0, 0, 0)
        self.chessboard[0][7] = Rook("Black", 0, 7, 0, 0)
        self.chessboard[7][0] = Rook("White", 7, 0, 0, 0)
        self.chessboard[7][7] = Rook("White", 7, 7, 0, 0)

    def create_jumpers(self):
        self.chessboard[0][1] = Jumper("Black", 0, 1, 0, 0)
        self.chessboard[0][6] = Jumper("Black", 0, 6, 0, 0)
        self.chessboard[7][1] = Jumper("White", 7, 1, 0, 0)
        self.chessboard[7][6] = Jumper("White", 7, 6, 0, 0)

    def create_bishops(self):
        self.chessboard[0][2] = Bishop("Black", 0, 2, 0, 0)
        self.chessboard[0][5] = Bishop("Black", 0, 5, 0, 0)
        self.chessboard[7][2] = Bishop("White", 7, 2, 0, 0)
        self.chessboard[7][5] = Bishop("White", 7, 5, 0, 0)

    def create_queens(self):
        self.chessboard[0][3] = Queen("Black", 0, 3, 0, 0)
        self.chessboard[7][3] = Queen("White", 7, 3, 0, 0)

    def create_kings(self):
        self.chessboard[0][4] = King("Black", 0, 4, 0, 0)
        self.chessboard[7][4] = King("White", 7, 4, 0, 0)

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

    def move(self, x, y):
        self.x = x
        self.y = y

    def remove_impossible_moves(self):
        for i in self.all_possible_moves[:]:
            if i[0] < 0 or i[0] > 7 or i[1] < 0 or i[1] > 7:
                self.all_possible_moves.remove(i)

    def __repr__(self):
        pass

    def get_all_moves(self):
        pass


class Pawn(Piece):

    def __init__(self, color, x, y, x_position, y_position):
        super().__init__(color, x, y, x_position, y_position)
        self.is_moved = False
        self.value = 1

    def __repr__(self):
        return f" {self.color[0]}P "

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

    def __repr__(self):
        return f" {self.color[0]}R "

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

    def __repr__(self):
        return f" {self.color[0]}J "

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

    def __repr__(self):
        return f" {self.color[0]}B "

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

    def __repr__(self):
        return f" {self.color[0]}Q "

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

    def __repr__(self):
        return f" {self.color[0]}K "

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

chessboard = Chessboard()
chessboard.create_pawns()
chessboard.create_rooks()
chessboard.create_jumpers()
chessboard.create_bishops()
chessboard.create_queens()
chessboard.create_kings()
chessboard.print_chessboard()