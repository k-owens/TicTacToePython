class GameBoard:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def set_board(self, board):
        self.board = board

    def change_square(self, square_number, player_number):
        self.board[square_number] = player_number

    def is_game_over(self):
        return self._did_someone_win() or self._is_board_full()

    def is_move_legal(self, move_number):
        return self.board[move_number] == 0

    def _is_board_full(self):
        return min(self.board) > 0

    def _did_someone_win(self):
        return self.did_player_win(1) or self.did_player_win(2)

    def did_player_win(self, player):
        return self._did_horizontal_win_happen(player) or self._did_vertical_win_happen(player) \
               or self._did_diagonal_win_happen(player)

    def _did_horizontal_win_happen(self, player):
        for index in range(0, 3):
            row = [self.board[3*index], self.board[3*index+1], self.board[3*index+2]]
            if self._did_win_occur(row, player):
                return True
        return False

    def _did_vertical_win_happen(self, player):
        for index in range(0, 3):
            row = [self.board[index], self.board[index+3], self.board[index+6]]
            if self._did_win_occur(row, player):
                return True
        return False

    def _did_diagonal_win_happen(self, player):
        _first_diagonal = [self.board[0], self.board[4], self.board[8]]
        _second_diagonal = [self.board[2], self.board[4], self.board[6]]
        return self._did_win_occur(_first_diagonal, player) or self._did_win_occur(_second_diagonal, player)

    def _did_win_occur(self, spaces, player):
        return spaces[0] == player and spaces[1] == player and spaces[2] == player
