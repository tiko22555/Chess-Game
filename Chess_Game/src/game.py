from src.coord import Coord
from src.board import Board
from src.exceptions import ChessGameException
from src.figures import Rook, Knight, Pawn, Bishop, Queen, King, ChessFigure


class ChessGame:
    def __init__(self):
        self.is_running = False
        self.board = None
        self.shax_color = None
        self.turn = None


    def start(self):
        self.is_running = True
        self.shax_color = False
        self.turn = "white"
        self.board = Board()
        self.board.organize()
        self.board.print()

        while self.is_running:
            try:
                current_position = input(f"[Turn: {self.turn}] Enter the position of the figure to move: ")
                if current_position == "exit":
                    self.is_running = False
                    break
                desired_position = input(f"[Turn: {self.turn}] Enter the desired position: ")
                if desired_position == "exit":
                    self.is_running = False
                    break

                current_coord = Coord(current_position)
                desired_coord = Coord(desired_position)

                if not isinstance(self.board[current_coord], ChessFigure):
                    raise ChessGameException("The field is empty!")

                figure = self.board[current_coord]
                if figure.color != self.turn:
                    raise ChessGameException("Invalid figure!")

                can_move = figure.move(self.board, current_coord, desired_coord)
                if not can_move:
                    raise ChessGameException("Invalid move!")

                if desired_coord.row in [0, 7] and isinstance(figure, Pawn):
                    new_figure_type = input("Enter new figure to replace (Queen, Bishop, Rook, Knight): ")
                    new_figure_type = new_figure_type.lower()
                    new_figure_color = figure.color
                    # if new_figure_type == 'queen':
                    #     new_figure = Queen(new_figure_color)
                    # elif new_figure_type == 'bishop':
                    #     new_figure = Bishop(new_figure_color)
                    # elif new_figure_type == 'rook':
                    #     new_figure = Rook(new_figure_color)
                    # elif new_figure_type == 'knight':
                    #     new_figure = Knight(new_figure_color)
                    figures_dict = {
                        'queen': Queen,
                        'bishop': Bishop,
                        'rook': Rook,
                        'knight': Knight,
                    }
                    figure_class = figures_dict[new_figure_type]
                    new_figure = figure_class(new_figure_color)
                    figure = new_figure

                temp_board = self.board.copy()
                temp_board[current_coord] = " "
                temp_board[desired_coord] = figure
                self.shax_color = self.check_shax(temp_board)
                if self.shax_color == self.turn:
                    raise ChessGameException("There is a check after your move. Try again!")
                del temp_board


                self.board[current_coord] = " "
                self.board[desired_coord] = figure
                print()
                self.board.print()
                self.shax_color = self.check_shax(self.board)

                if self.turn == "white":
                    self.turn = "black"
                else:
                    self.turn = "white"
            except ChessGameException as error:
                print(error)


    @staticmethod
    def check_shax(board):
        white_king_coord = None
        black_king_coord = None

        for i in range(len(board.board_matrix)):
            for j in range(len(board.board_matrix[i])):
                field = board.board_matrix[i][j]
                if isinstance(field, King):
                    if field.color == 'white':
                        white_king_coord = Coord.from_coords(i, j)
                    else:
                        black_king_coord = Coord.from_coords(i, j)
        for i in range(len(board.board_matrix)):
            for j in range(len(board.board_matrix[i])):
                field = board.board_matrix[i][j]
                if not isinstance(field, ChessFigure):
                    continue
                figure = field
                if figure.color == 'white':
                    opposite_king_coord = black_king_coord
                    opposite_color = 'black'
                else:
                    opposite_king_coord = white_king_coord
                    opposite_color = 'white'
                current_coord = Coord.from_coords(i, j)
                can_attack_king = figure.move(board, current_coord, opposite_king_coord)
                if can_attack_king:
                    print(f"Shaxh! The {opposite_color} King is under attack!")
                    return opposite_color
        return ''
