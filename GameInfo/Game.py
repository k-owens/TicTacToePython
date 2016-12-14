class Game:
    def __init__(self, player1, player2, game_board, turn=1):
        self.player1 = player1
        self.player2 = player2
        self.game_board = game_board
        self.turn = turn

    def process_turn(self):
        if self.turn % 2 == 1:
            self._take_turn(self.player1)

        else:
            self._take_turn(self.player2)

    def _take_turn(self, player):
        move = player.make_move(self.game_board)
        if self.game_board.is_move_legal(move):
            self.game_board.change_square(move, player.player_number)
            self.turn += 1
