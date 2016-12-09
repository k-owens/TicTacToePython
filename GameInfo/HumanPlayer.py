class HumanPlayer:
    def __init__(self, player_number, input_process):
        self.player_number = player_number
        self.input_process = input_process

    def make_move(self, current_board):
        self.input_process.display_game(current_board)
        self.input_process.ask_user_for_input()
        return self.input_process.get_move_input()
