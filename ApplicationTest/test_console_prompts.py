from unittest import TestCase
from Application import console_prompts
from GameInfo import game_board
from GameInfo import game
from GameInfo import computer_player


class TestConsolePrompts(TestCase):
    def test_asking_for_input(self):
        self.assertEqual(console_prompts.ConsolePrompts().ask_user_for_input(), "Move options: \r\n"
                                                                                + "0|1|2\r\n"
                                                                                + "_____\r\n"
                                                                                + "3|4|5\r\n"
                                                                                + "_____\r\n"
                                                                                + "6|7|8\r\n"
                                                                                + "Please enter the move number: ")

    def test_game_display(self):
        board = game_board.GameBoard()
        board.change_square(1, 1)
        board.change_square(3, 1)
        board.change_square(7, 2)
        board.change_square(8, 2)
        self.assertEqual(console_prompts.ConsolePrompts().display_game(board), "Current board: \r\n"
                                                                            + " |O| \r\n"
                                                                            + "_____\r\n"
                                                                            + "O| | \r\n"
                                                                            + "_____\r\n"
                                                                            + " |X|X\r\n")

    def test_turn_display_player1(self):
        player1 = computer_player.ComputerPlayer(1)
        player2 = computer_player.ComputerPlayer(2)
        board = game_board.GameBoard()
        test_game = game.Game(player1, player2, board)
        self.assertEqual(console_prompts.ConsolePrompts().alert_whose_turn_it_is(test_game), "Player 1's turn... ")

    def test_turn_display_player2(self):
        player1 = computer_player.ComputerPlayer(1)
        player2 = computer_player.ComputerPlayer(2)
        board = game_board.GameBoard()
        test_game = game.Game(player1, player2, board)
        test_game.process_turn()
        self.assertEqual(console_prompts.ConsolePrompts().alert_whose_turn_it_is(test_game), "Player 2's turn... ")

    def test_bad_input(self):
        self.assertEqual(console_prompts.ConsolePrompts().alert_bad_input(),
                         "Input is invalid. Please enter a number on the board.")

    def test_game_over_alert_player1(self):
        board = game_board.GameBoard()
        board.set_board([1, 1, 1, 0, 0, 2, 2, 2, 0])
        self.assertEqual(console_prompts.ConsolePrompts().alert_game_over(board), "Player 1 has won!")

    def test_game_over_alert_player2(self):
        board = game_board.GameBoard()
        board.set_board([1, 1, 0, 1, 0, 0, 2, 2, 2])
        self.assertEqual(console_prompts.ConsolePrompts().alert_game_over(board), "Player 2 has won!")

    def test_game_over_alert_tie_game(self):
        board = game_board.GameBoard()
        board.set_board([1, 2, 1, 1, 2, 1, 2, 1, 2])
        self.assertEqual(console_prompts.ConsolePrompts().alert_game_over(board), "Tie game!")
