from Application import console_prompts
from Application import human_input
from Application import input_output
from GameInfo import game
from GameInfo import human_player
from GameInfo import computer_player
from GameInfo import game_board


console_io = input_output.InputOutput(human_input.HumanInput(), console_prompts.ConsolePrompts())
player1 = human_player.HumanPlayer(1, console_io)
player2 = computer_player.ComputerPlayer(2)
_game = game.Game(player1, player2, game_board.GameBoard())

while not _game.game_board.is_game_over():
    console_io.alert_whose_turn_it_is(_game)
    console_io.display_game(_game.game_board)
    _game.process_turn()

console_io.alert_game_over(_game.game_board)
console_io.display_game(_game.game_board)
