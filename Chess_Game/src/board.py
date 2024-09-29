import copy

from src.figures import Rook, Knight, Pawn, Bishop, Queen, King

class Board:
    def __init__(self):
        self.board_matrix = [[' '] * 8] * 8

    def organize(self):
        self.board_matrix = [
            [Rook("black"), Knight("black"), Bishop("black"), Queen("black"), King("black"), Bishop("black"), Knight("black"), Rook("black")],
            [Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"),],
            [" ", " ", " ", " ", " ", " ", " ", " ", ],
            [" ", " ", " ", " ", " ", " ", " ", " ", ],
            [" ", " ", " ", " ", " ", " ", " ", " ", ],
            [" ", " ", " ", " ", " ", " ", " ", " ", ],
            [Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"),],
            [Rook("white"), Knight("white"), Bishop("white"), Queen("white"), King("white"), Bishop("white"), Knight("white"), Rook("white")]
        ]

    def organize_for_tests(self):
        self.board_matrix = [
            [" ", Knight("black"), Bishop("black"), " ", King("black"), " ", Knight("black"), Rook("black")],
            [Pawn("black"), Pawn("black"), King("white"), Pawn("black"), Pawn("black"), Pawn("black"), " ", Pawn("black"),],
            [" ", " ", Pawn("white"), " ", Bishop("black"), Knight("white"), " ", " ", ],
            [" ", " ", " ", " ", " ", " ", Pawn("black"), Pawn("white"), ],
            [Rook("white"), " ", Queen("black"), Queen("white"), " ", " ", " ", Rook("black"), ],
            [" ", " ", " ", Pawn("white"), " ", " ", Pawn("black"), Pawn("white"), ],
            [Pawn("white"), " ", Pawn("white"), " ", Pawn("white"), " ", Pawn("white"), " ",],
            [" ", Knight("white"), Bishop("white"), " ", " ", Bishop("white"), " ", Rook("white")]
        ]


    def organize_for_castling_testing(self):
        self.board_matrix = [
            [Rook("black"), Knight("black"), Bishop("black"), Queen("black"), King("black"), Bishop("black"), Knight("black"), Rook("black")],
            [Pawn("white"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"),],
            [" ", " ", " ", " ", " ", " ", " ", " ", ],
            [" ", " ", " ", " ", " ", " ", " ", " ", ],
            [" ", " ", " ", " ", " ", " ", " ", " ", ],
            [" ", " ", " ", " ", " ", " ", " ", " ", ],
            [Pawn("black"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"),],
            [Rook("white"), " ", " ", " ", King("white"), Bishop("white"), Knight("white"), Rook("white")]
        ]

    def organize_for_check_testing(self):
        self.board_matrix = [
            [Rook("black"), Knight("black"), " ", Queen("black"), King("black"), Bishop("black"), Knight("black"), Rook("black")],
            [Pawn("black"), Pawn("black"), Pawn("black"), " ", Pawn("black"), Pawn("black"), Pawn("black"), Pawn("black"),],
            [" ", " ", " ", " ", " ", " ", " ", Pawn("black"), ],
            [" ", " ", " ", " ", " ", " ", " ", " ", ],
            [" ", " ", " ", " ", " ", " ", " ", " ", ],
            [" ", " ", Bishop("black"), " ", " ", " ", " ", " ", ],
            [Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"), Pawn("white"),],
            [Rook("white"), Knight("white"), Bishop("white"), Queen("white"), King("white"), Bishop("white"), Knight("white"), Rook("white")]
        ]

    def print(self):
        letters = "    A   B   C   D   E   F   G   H"
        line = "   -------------------------------"
        template = "{0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {0}"
        print(letters)
        print(line)
        for i in range(8):
            print(template.format(8-i, *self.board_matrix[i]))
            print(line)
        print(letters)

    def copy(self):
        new_board = Board()
        new_board.board_matrix = copy.deepcopy(self.board_matrix)
        return new_board

    def __getitem__(self, coord):
        return self.board_matrix[coord.row][coord.column]

    def __setitem__(self, coord, value):
        self.board_matrix[coord.row][coord.column] = value
