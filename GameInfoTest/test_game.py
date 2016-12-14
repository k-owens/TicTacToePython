from unittest import TestCase
from .test_player import TestPlayer
from GameInfo import game
from GameInfo import game_board


class TestGame(TestCase):
    def test_player1_can_make_a_move(self):
        test_player = TestPlayer(1, 0)
        test_player2 = TestPlayer(2, 1)
        test_game = game.Game(test_player, test_player2, game_board.GameBoard())
        test_game.process_turn()
        self.assertEqual(test_game.game_board.board, [1, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_player2_can_make_a_move(self):
        test_player = TestPlayer(1, 0)
        test_player2 = TestPlayer(2, 1)
        test_game = game.Game(test_player, test_player2, game_board.GameBoard())
        test_game.process_turn()
        test_game.process_turn()
        self.assertEqual(test_game.game_board.board, [1, 2, 0, 0, 0, 0, 0, 0, 0])

    def test_game_will_not_move_forward_with_illegal_move(self):
        test_player = TestPlayer(1, 0)
        test_player2 = TestPlayer(2, 0)
        test_game = game.Game(test_player, test_player2, game_board.GameBoard())
        test_game.process_turn()
        test_game.process_turn()
        self.assertEqual(test_game.game_board.board, [1, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(test_game.turn, 2)
