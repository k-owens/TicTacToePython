from unittest import TestCase
from GameInfo import GameBoard
from GameInfo import ComputerPlayer


class TestComputerPlayer(TestCase):
    def test_computer_makes_correct_move(self):
        computer_player = ComputerPlayer.ComputerPlayer(2)
        board = GameBoard.GameBoard([1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(computer_player.make_move(board), 4)

    def test_computer_makes_correct_move2(self):
        computer_player = ComputerPlayer.ComputerPlayer(2)
        board = GameBoard.GameBoard([1, 0, 1, 0, 2, 0, 0, 0, 0])
        self.assertEqual(computer_player.make_move(board), 1)

    def test_computer_makes_correct_move3(self):
        computer_player = ComputerPlayer.ComputerPlayer(1)
        board = GameBoard.GameBoard([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(computer_player.make_move(board), 0)

    def test_computer_makes_correct_move4(self):
        computer_player = ComputerPlayer.ComputerPlayer(1)
        board = GameBoard.GameBoard([2, 0, 2, 1, 0, 1, 0, 0, 0])
        self.assertEqual(computer_player.make_move(board), 4)

    def test_computer_makes_correct_move5(self):
        computer_player = ComputerPlayer.ComputerPlayer(2)
        board = GameBoard.GameBoard([1, 0, 0, 0, 2, 0, 0, 0, 1])
        self.assertEqual(computer_player.make_move(board), 1)
