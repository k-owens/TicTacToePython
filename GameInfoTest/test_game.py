from unittest import TestCase
from .TestPlayer import TestPlayer
from GameInfo import Game


class TestGame(TestCase):
    def test_player1_can_make_a_move(self):
        test_player = TestPlayer(1, 0)
        test_player2 = TestPlayer(2, 1)
        game = Game.Game(test_player, test_player2)
        game.process_turn()
        self.assertEqual(game.game_board.board, [1, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_player2_can_make_a_move(self):
        test_player = TestPlayer(1, 0)
        test_player2 = TestPlayer(2, 1)
        game = Game.Game(test_player, test_player2)
        game.process_turn()
        game.process_turn()
        self.assertEqual(game.game_board.board, [1, 2, 0, 0, 0, 0, 0, 0, 0])
