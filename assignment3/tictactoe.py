class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Board:
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        self.board_array = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = "X"

    def __str__(self):
        lines = []
        lines.append(f"{self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]}\n")
        lines.append("-----------\n")
        lines.append(f"{self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]}\n")
        lines.append("-----------\n")
        lines.append(f"{self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]}\n")
        return "".join(lines)

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")

        move_index = Board.valid_moves.index(move_string)
        row = move_index // 3
        column = move_index % 3

        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")

        self.board_array[row][column] = self.turn
        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                    break
            if not cat:
                break

        if cat:
            return (True, "Cat's Game.")

        win = False

        # rows
        for i in range(3):
            if self.board_array[i][0] != " " and \
               self.board_array[i][0] == self.board_array[i][1] == self.board_array[i][2]:
                win = True
                break

        # columns
        if not win:
            for i in range(3):
                if self.board_array[0][i] != " " and \
                   self.board_array[0][i] == self.board_array[1][i] == self.board_array[2][i]:
                    win = True
                    break

        # diagonals
        if not win:
            if self.board_array[1][1] != " ":
                if self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2]:
                    win = True
                if self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0]:
                    win = True

        if not win:
            return (False, f"{self.turn}'s turn.")
        else:
            winner = "O" if self.turn == "X" else "X"
            return (True, f"{winner} wins!")

# Main Game Logic
if __name__ == "__main__":
    game_board = Board()
    is_game_over = False

    print("Welcome to Tic-Tac-Toe!")
    print(game_board)

    while not is_game_over:
        status = game_board.whats_next()
        is_game_over = status[0]
        message = status[1]

        if is_game_over:
            print(f"\nGame Over! {message}")
            break
            
        print(f"\n{message}")
        user_move = input("Enter your move (e.g., 'upper left', 'center'): ").strip().lower()

        try:
            game_board.move(user_move)
            print("\n" + str(game_board))
        except TictactoeException as e:
            print(f"\nOops! {e.message} Please try again.")
