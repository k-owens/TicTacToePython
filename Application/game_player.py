from GameInfo import game
from GameInfo import human_player
from Application import human_input

playerInput = human_input.HumanInput()
player1 = human_player.HumanPlayer(1, playerInput)
player2 = human_player.HumanPlayer(2, playerInput)
_game = game.Game(player1, player2)

while not _game.game_board.is_game_over():
    _game.process_turn()
