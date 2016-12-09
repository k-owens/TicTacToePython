from unittest import TestCase
from GameInfo import human_player
from .mock_input import MockInput
from GameInfo import game_board


class TestHumanPlayer(TestCase):
    def test_make_move(self):
        human = human_player.HumanPlayer(1, MockInput())
        board = game_board.GameBoard()
        human.make_move(board)
        self.assertEqual(human.make_move(board), 0)
