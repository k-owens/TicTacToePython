import copy


class ComputerPlayer:
    def __init__(self, player_number):
        self.player_number = player_number

    def make_move(self, current_board):
        move_scores = []
        for i in range(0, 9):
            if current_board.board[i] == 0:
                next_board = copy.copy(current_board)
                next_board.change_square(i, self.player_number) #need to change this later to allow for first or second player
                move_scores.append(self._minimax(next_board, False))
                next_board.change_square(i, 0)
            else:
                move_scores.append(-2)
        return move_scores.index(max(move_scores))

                        #this is an object(GameBoard)
    def _minimax(self, current_board, maximizing_player):
        if current_board.did_player_win(self.player_number):
            return 1
        elif current_board.did_player_win(self._other_number()):
            return -1
        elif current_board.is_game_over():
            return 0
        elif maximizing_player:
            best_score = -2
            for i in range(0, 9):
                if current_board.board[i] == 0:
                    next_board = copy.copy(current_board)
                    next_board.change_square(i, self.player_number) #possibly need to change this (should it have the player number?)
                    move_score = self._minimax(next_board, False)
                    #print("best: " + str(move_score))
                    #print(next_board.board)
                    if move_score > best_score:
                        best_score = move_score
                    next_board.change_square(i, 0)
            return best_score
        else:  #minimizing player
            worst_score = 2
            for i in range(0, 9):
                if current_board.board[i] == 0:
                    next_board = copy.copy(current_board)
                    next_board.change_square(i, self._other_number()) #possibly need to change this (should it have the player number?)
                    move_score = self._minimax(next_board, True)
                    #print("worst: " + str(move_score))
                    #print(next_board.board)
                    if move_score < worst_score:
                        worst_score = move_score
                    next_board.change_square(i, 0)
            return worst_score

    def _other_number(self):
        if self.player_number == 1:
            return 2
        else:
            return 1
