class ConsolePrompts:
    def ask_user_for_input(self):
        return "Move options: \r\n"\
            + "0|1|2\r\n"\
            + "_____\r\n"\
            + "3|4|5\r\n"\
            + "_____\r\n"\
            + "6|7|8\r\n"\
            + "Please enter the move number: "

    def display_game(self, current_board):
        board_with_symbols = self._convert_board(current_board.board)
        return "Current board: \r\n"\
            + str(board_with_symbols[0]) + "|" + str(board_with_symbols[1]) + "|" + str(board_with_symbols[2] + "\r\n")\
            + "_____\r\n"\
            + str(board_with_symbols[3]) + "|" + str(board_with_symbols[4]) + "|" + str(board_with_symbols[5] + "\r\n")\
            + "_____\r\n"\
            + str(board_with_symbols[6]) + "|" + str(board_with_symbols[7]) + "|" + str(board_with_symbols[8] + "\r\n")

    def alert_whose_turn_it_is(self, game):
        if game.turn % 2 == 1:
            return "Player 1's turn... "
        return "Player 2's turn... "

    def alert_bad_input(self):
        return "Input is invalid. Please enter a number on the board."

    def alert_game_over(self, game_board):
        if game_board.did_player_win(1):
            return "Player 1 has won!"
        elif game_board.did_player_win(2):
            return "Player 2 has won!"
        return "Tie game!"

    def _convert_board(self, board):
        converted_board = []
        for index in range(0, 9):
            if board[index] == 0:
                converted_board.append(' ')
            elif board[index] == 1:
                converted_board.append('O')
            else:
                converted_board.append('X')
        return converted_board
