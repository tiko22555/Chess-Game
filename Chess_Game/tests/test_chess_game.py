from src.board import Board
from src.coord import Coord


def test_king_moves(board):
    c = Coord("C7") #King
    x = board[c]
    assert x.move(board, Coord("C7"), Coord("A5")) == False
    assert x.move(board, Coord("C7"), Coord("B7")) == True
    assert x.move(board, Coord("C7"), Coord("C8")) == True
    assert x.move(board, Coord("C7"), Coord("D6")) == True
    assert x.move(board, Coord("C7"), Coord("C6")) == False


def test_queen_moves(board):
    c = Coord("D4") #Queen
    x = board[c]
    assert x.move(board, Coord("D4"), Coord("D3")) == False
    assert x.move(board, Coord("D4"), Coord("H4")) == True
    assert x.move(board, Coord("D4"), Coord("G1")) == True
    assert x.move(board, Coord("D4"), Coord("G4")) == True
    assert x.move(board, Coord("D4"), Coord("F5")) == False


def test_bishop_moves(board):
    c = Coord("E6") #Bishop
    x = board[c]
    assert x.move(board, Coord("E6"), Coord("E3")) == False
    assert x.move(board, Coord("E6"), Coord("H3")) == True
    assert x.move(board, Coord("E6"), Coord("G4")) == True
    assert x.move(board, Coord("E6"), Coord("C4")) == False


def test_rook_moves(board):
    c = Coord("A4") #Rook
    x = board[c]
    assert x.move(board, Coord("A4"), Coord("B3")) == False
    assert x.move(board, Coord("A4"), Coord("C4")) == True
    assert x.move(board, Coord("A4"), Coord("A6")) == True
    assert x.move(board, Coord("A4"), Coord("A2")) == False
    assert x.move(board, Coord("A4"), Coord("E4")) == False


def test_king_moves(board):
    c = Coord("F6") #Knight
    x = board[c]
    assert x.move(board, Coord("F6"), Coord("F3")) == False
    assert x.move(board, Coord("F6"), Coord("G8")) == True
    assert x.move(board, Coord("F6"), Coord("E4")) == True
    assert x.move(board, Coord("F6"), Coord("H5")) == False


def test_pawn_tests(board):
    c = Coord("D3") #Pawn
    x = board[c]
    assert x.move(board, Coord("D3"), Coord("D4")) == False
    assert x.move(board, Coord("D3"), Coord("C4")) == True
    assert x.move(board, Coord("D3"), Coord("D2")) == False
    assert x.move(board, Coord("D3"), Coord("C2")) == False
    c1 = Coord("E2")
    x = board[c1]
    assert x.move(board, Coord("E2"), Coord("E3")) == True


def run_tests():
    board = Board()
    board.organize_for_tests()

    test_king_moves(board)
    test_queen_moves(board)
    test_bishop_moves(board)
    test_rook_moves(board)
    test_king_moves(board)
    test_pawn_tests(board)

    print("All tests passed!")
