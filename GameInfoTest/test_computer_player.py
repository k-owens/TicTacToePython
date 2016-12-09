from unittest import TestCase
from GameInfo import game_board
from GameInfo import computer_player


class TestComputerPlayer(TestCase):
    def test_computer_makes_correct_move(self):
        ai_player = computer_player.ComputerPlayer(2)
        board = game_board.GameBoard([1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(ai_player.make_move(board), 4)

    def test_computer_makes_correct_move2(self):
        ai_player = computer_player.ComputerPlayer(2)
        board = game_board.GameBoard([1, 0, 1, 0, 2, 0, 0, 0, 0])
        self.assertEqual(ai_player.make_move(board), 1)

    def test_computer_makes_correct_move3(self):
        ai_player = computer_player.ComputerPlayer(1)
        board = game_board.GameBoard([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(ai_player.make_move(board), 0)

    def test_computer_makes_correct_move4(self):
        ai_player = computer_player.ComputerPlayer(1)
        board = game_board.GameBoard([2, 0, 2, 1, 0, 1, 0, 0, 0])
        self.assertEqual(ai_player.make_move(board), 4)

    def test_computer_makes_correct_move5(self):
        ai_player = computer_player.ComputerPlayer(2)
        board = game_board.GameBoard([1, 0, 0, 0, 2, 0, 0, 0, 1])
        self.assertEqual(ai_player.make_move(board), 1)
