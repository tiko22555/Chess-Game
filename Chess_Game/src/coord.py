from src.exceptions import ChessGameException

class Coord:
    def __init__(self, coord_str):
        if len(coord_str) != 2 or not coord_str[0].isalpha() or not coord_str[1].isdigit():
            raise ChessGameException("Invalid Value")
        column = ord(coord_str[0].upper()) - ord('A')
        row = 8 - int(coord_str[1])
        if not (0 <= row < 8) or not (0 <= column < 8):
            raise ChessGameException("Invalid Value")
        self.row = row
        self.column = column

    def __repr__(self):
        return f"({self.row}, {self.column})"

    @classmethod
    def from_coords(cls, row, column):
        coord = cls("A4")
        coord.row = row
        coord.column = column
        return coord
