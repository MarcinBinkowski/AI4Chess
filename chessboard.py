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

    def __str__(self):
        pass

    def move(self, x, y):
        if self.validate_move:
            self.x = x
            self.y = y
            return True
        return False

    def validate_move(self):
        pass


class Pawn(Piece):

    def __str__(self):
        return "Pawn"


a = Pawn(1,2)




#chessboard = Chessboard()
#chessboard.print_chessboard()