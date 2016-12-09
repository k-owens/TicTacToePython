from .GameBoard import GameBoard


class Game:
    def __init__(self, player1, player2, game_board=GameBoard(), turn=1):
        self.player1 = player1
        self.player2 = player2
        self.game_board = game_board
        self.turn = turn

    def process_turn(self):
        if self.turn % 2 == 1:
            self.game_board.change_square(self.player1.make_move(self.game_board), self.player1.player_number)
            self.turn += 1
        else:
            self.game_board.change_square(self.player2.make_move(self.game_board), self.player2.player_number)
            self.turn += 1
