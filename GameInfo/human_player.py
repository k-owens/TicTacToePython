class HumanPlayer:
    def __init__(self, player_number, input_and_output_process):
        self.player_number = player_number
        self.input_and_output_process = input_and_output_process

    def make_move(self, current_board):
        self.input_and_output_process.ask_user_for_input()
        return self.input_and_output_process.get_move_input(current_board)
