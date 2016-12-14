class HumanInput:
    def get_move_input(self, current_board):
        try:
            move = int(input(""))
            if move < 0 or move > 8:
                print(self._alert_bad_input())
                return self.get_move_input(current_board)
            elif current_board.is_move_legal(move):
                return move
            print(self._alert_illegal_move())
            return self.get_move_input(current_board)
        except:
            print(self._alert_bad_input())
            return self.get_move_input(current_board)

    def _alert_illegal_move(self):
        return "Move is illegal. Please enter a move that has not already been made."

    def _alert_bad_input(self):
        return "Input is invalid. Please enter a number on the board."
