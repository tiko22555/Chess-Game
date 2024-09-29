from src.coord import Coord

class ChessFigure:
    def __init__(self, color):
        if color not in ("white", "black"):
            raise ValueError("Invalid color")
        self.color = color

    def _check_fields_between(self, board, current_coords, desired_coords):
        row_diff, col_diff = self._get_row_and_col_diffs(current_coords, desired_coords)
        if desired_coords.row - current_coords.row != 0:
            row_i = int(
                (desired_coords.row - current_coords.row)
                /
                abs(desired_coords.row - current_coords.row)
            )
        else:
            row_i = 0
        if desired_coords.column - current_coords.column != 0:
            column_i = int(
                (desired_coords.column - current_coords.column)
                /
                abs(desired_coords.column - current_coords.column)
            ) 
        else:
            column_i = 0

        for i in range(1, max([row_diff, col_diff])):
            observe_i = current_coords.row + (i * row_i)
            observe_j = current_coords.column + (i * column_i)
            observe_coord = Coord.from_coords(observe_i, observe_j)
            observe_figure = board[observe_coord]
            if isinstance(observe_figure, ChessFigure):
                return False
        return True

    def _get_row_and_col_diffs(self, current_coords, desired_coords):
        row_diff = abs(desired_coords.row - current_coords.row)
        col_diff = abs(desired_coords.column - current_coords.column)
        return row_diff, col_diff


class Rook(ChessFigure):
    def __init__(self, color):
        super().__init__(color)
        self.has_moved = False

    def __repr__(self):
        if self.color == "white":
            return "♜"
        else:
            return "♖"

    def move(self, board, current_coords, desired_coords):
        row_diff, col_diff = self._get_row_and_col_diffs(current_coords, desired_coords)

        is_move_right = (row_diff == 0 and col_diff > 0) or (row_diff > 0 and col_diff == 0)
        if not is_move_right:
            return False

        if not self._check_fields_between(board, current_coords, desired_coords):
            return False

        observe_figure_last = board[desired_coords]
        can_move = (
            not isinstance(observe_figure_last, ChessFigure)
            or self.color != observe_figure_last.color
        )
        if not can_move:
            return False
        self.has_moved = True
        return True


class Knight(ChessFigure):
    def __repr__(self):
        if self.color == "white":
            return "♞"
        else:
            return "♘"

    def move(self, board, current_coords, desired_coords):
        row_diff, col_diff = self._get_row_and_col_diffs(current_coords, desired_coords)
        is_move_right = (row_diff == 1 and col_diff == 2) or (row_diff == 2 and col_diff == 1)
        if not is_move_right:
            return False
        last_figure = board[desired_coords]
        return (
            not isinstance(last_figure, ChessFigure)
            or self.color != last_figure.color
        )


class Bishop(ChessFigure):
    def __repr__(self):
        if self.color == "white":
            return "♝"
        else:
            return "♗"

    def move(self, board, current_coords, desired_coords):
        row_diff, col_diff = self._get_row_and_col_diffs(current_coords, desired_coords)

        is_move_right = (row_diff == col_diff != 0)
        if not is_move_right:
            return False

        if not self._check_fields_between(board, current_coords, desired_coords):
            return False


        observe_figure_last = board[desired_coords]
        return (
            not isinstance(observe_figure_last, ChessFigure)
            or self.color != observe_figure_last.color
        )



class Queen(ChessFigure):
    def __repr__(self):
        if self.color == "white":
            return "♛"
        else:
            return "♕"

    def move(self, board, current_coords, desired_coords):
        row_diff, col_diff = self._get_row_and_col_diffs(current_coords, desired_coords)

        is_move_right = (row_diff == 0 and col_diff > 0) or (row_diff > 0 and col_diff == 0) or (row_diff == col_diff != 0)
        if not is_move_right:
            return False

        if not self._check_fields_between(board, current_coords, desired_coords):
            return False

        observe_figure_last = board[desired_coords]
        return (
            not isinstance(observe_figure_last, ChessFigure)
            or self.color != observe_figure_last.color
        )


class King(ChessFigure):
    def __init__(self, color):
        super().__init__(color)
        self.has_moved = False

    def __repr__(self):
        if self.color == "white":
            return "♚"
        else:
            return "♔"

    def move(self, board, current_coords, desired_coords):
        row_diff, col_diff = self._get_row_and_col_diffs(current_coords, desired_coords)
        is_move_right = (row_diff == 1 and col_diff <= 1) or (col_diff == 1 and row_diff <= 1)

        if is_move_right:
            can_move = (
                board[desired_coords] == " "
                or board[desired_coords].color != self.color
            )
            if not can_move:
                return False
            self.has_moved = True
            return True
        if not self.has_moved and row_diff == 0 and col_diff == 2:
            has_castled = self.castling(board, current_coords, desired_coords)
            return has_castled
        return False

    def castling(self, board, current_coords, desired_coords):
        is_left = current_coords.column - desired_coords.column > 0

        column = "1" if self.color == "white" else "8"
        if is_left:
            castling_rook_coord = Coord(f"A{column}")
            rook_desired_coord = Coord(f"D{column}")
        else:
            castling_rook_coord = Coord(f"H{column}")
            rook_desired_coord = Coord(f"F{column}")

        castling_rook = board[castling_rook_coord]
        if isinstance(castling_rook, Rook) and castling_rook.has_moved == False:
            are_fields_empty = self._check_fields_between(board, current_coords, castling_rook_coord)
            if are_fields_empty:
                can_rook_move = castling_rook.move(board, castling_rook_coord, rook_desired_coord)
                if can_rook_move:
                    board[castling_rook_coord] = " "
                    board[rook_desired_coord] = castling_rook
                    return True
        return False


class Pawn(ChessFigure):
    def __repr__(self):
        if self.color == "white":
            return "♟"
        else:
            return "♙"

    def move(self, board, current_coords, desired_coords): 
        row_diff, col_diff = self._get_row_and_col_diffs(current_coords, desired_coords)

        if self.color == "white":
            if current_coords.row == 6:
                step_size = [1, 2]
            else:
                step_size = [1]

            if ((current_coords.row - desired_coords.row) == 1
                and col_diff == 1
                and board[desired_coords] != " "
                and board[desired_coords].color != self.color):
                return True

            if ((current_coords.row - desired_coords.row) in step_size
                and current_coords.column == desired_coords.column
                and board[desired_coords] == " "):
                return True
        else:
            if current_coords.row == 1:
                step_size = [-2, -1]
            else:
                step_size = [-1]

  
            if ((current_coords.row - desired_coords.row) == -1
                and col_diff == 1
                and board[desired_coords] != " "
                and board[desired_coords].color != self.color):
                return True
 
            if ((current_coords.row - desired_coords.row) in step_size
                and current_coords.column == desired_coords.column
                and board[desired_coords] == " "):
                return True
        return False
