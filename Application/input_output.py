class InputOutput:
    def __init__(self, input_process, display):
        self.input_process = input_process
        self.display = display

    def get_move_input(self, current_board):
        return self.input_process.get_move_input(current_board)

    def ask_user_for_input(self):
        print(self.display.ask_user_for_input())

    def display_game(self, current_board):
        print(self.display.display_game(current_board))

    def alert_whose_turn_it_is(self, game):
        print(self.display.alert_whose_turn_it_is(game))

    def alert_game_over(self, game_board):
        print(self.display.alert_game_over(game_board))
