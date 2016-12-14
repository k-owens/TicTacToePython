import copy


class ComputerPlayer:
    def __init__(self, player_number):
        self.player_number = player_number

    def make_move(self, current_board):
        move_scores = []
        for i in range(0, 9):
            if current_board.board[i] == 0:
                next_board = copy.copy(current_board)
                next_board.change_square(i, self.player_number)
                move_scores.append(self._minimax(next_board, False))
                next_board.change_square(i, 0)
            else:
                move_scores.append(-2)
        return move_scores.index(max(move_scores))

    def _minimax(self, current_board, maximizing_player):
        if current_board.did_player_win(self.player_number):
            return 1
        elif current_board.did_player_win(self._other_number()):
            return -1
        elif current_board.is_game_over():
            return 0
        elif maximizing_player:
            return self._maximize_move(current_board)
        else:
            return self._minimize_move(current_board)

    def _maximize_move(self, current_board):
        best_score = -2
        for i in range(0, 9):
            if current_board.board[i] == 0:
                next_board = copy.copy(current_board)
                next_board.change_square(i, self.player_number)
                move_score = self._minimax(next_board, False)
                if move_score > best_score:
                    best_score = move_score
                next_board.change_square(i, 0)
        return best_score

    def _minimize_move(self, current_board):
        worst_score = 2
        for i in range(0, 9):
            if current_board.board[i] == 0:
                next_board = copy.copy(current_board)
                next_board.change_square(i, self._other_number())
                move_score = self._minimax(next_board, True)
                if move_score < worst_score:
                    worst_score = move_score
                next_board.change_square(i, 0)
        return worst_score

    def _other_number(self):
        if self.player_number == 1:
            return 2
        else:
            return 1
