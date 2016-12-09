from unittest import TestCase
from GameInfo import GameBoard
import copy


class TestGameBoard(TestCase):
    def test_game_does_not_end_early(self):
        _game_board = GameBoard.GameBoard()
        self.assertFalse(_game_board.is_game_over())

    def test_game_does_not_end_early2(self):
        _game_board = GameBoard.GameBoard([1, 2, 1, 0, 0, 0, 0, 0, 0])
        self.assertFalse(_game_board.is_game_over())

    def test_game_ends_with_full_board(self):
        _game_board = GameBoard.GameBoard([1, 2, 1, 2, 1, 2, 2, 1, 1])
        self.assertTrue(_game_board.is_game_over())

    def test_game_ends_with_horizontal_win(self):
        _game_board = GameBoard.GameBoard([1, 1, 1, 0, 0, 0, 0, 0, 0])
        _game_board2 = GameBoard.GameBoard([0, 0, 0, 2, 2, 2, 0, 0, 0])
        _game_board3 = GameBoard.GameBoard([0, 0, 0, 0, 0, 0, 1, 1, 1])
        self.assertTrue(_game_board.is_game_over())
        self.assertTrue(_game_board2.is_game_over())
        self.assertTrue(_game_board3.is_game_over())

    def test_game_ends_with_vertical_win(self):
        _game_board = GameBoard.GameBoard([1, 0, 0, 1, 0, 0, 1, 0, 0])
        _game_board2 = GameBoard.GameBoard([0, 2, 0, 0, 2, 0, 0, 2, 0])
        _game_board3 = GameBoard.GameBoard([0, 0, 1, 0, 0, 1, 0, 0, 1])
        self.assertTrue(_game_board.is_game_over())
        self.assertTrue(_game_board2.is_game_over())
        self.assertTrue(_game_board3.is_game_over())

    def test_game_ends_with_diagonal_win(self):
        _game_board = GameBoard.GameBoard([1, 0, 0, 0, 1, 0, 0, 0, 1])
        _game_board2 = GameBoard.GameBoard([0, 0, 2, 0, 2, 0, 2, 0, 0])
        self.assertTrue(_game_board.is_game_over())
        self.assertTrue(_game_board2.is_game_over())

    def test_board_can_be_changed(self):
        _game_board = GameBoard.GameBoard()
        _game_board.change_square(0, 1)
        _game_board.change_square(1, 2)
        self.assertEqual(_game_board.board, [1, 2, 0, 0, 0, 0, 0, 0, 0])
