from GameInfo import Game
from GameInfo import HumanPlayer
from Application import HumanInput

playerInput = HumanInput.HumanInput()
player1 = HumanPlayer.HumanPlayer(1, playerInput)
player2 = HumanPlayer.HumanPlayer(2, playerInput)
game = Game.Game(player1, player2)

while not game.game_board.is_game_over():
    game.process_turn()
