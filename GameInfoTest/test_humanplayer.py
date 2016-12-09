from unittest import TestCase
from GameInfo import HumanPlayer
from .MockInput import MockInput
from GameInfo import GameBoard


class TestHumanPlayer(TestCase):
    def test_make_move(self):
        human = HumanPlayer.HumanPlayer(1, MockInput())
        game_board = GameBoard.GameBoard()
        human.make_move(game_board)
        self.assertEqual(human.make_move(game_board), 0)
