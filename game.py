from board import Board
from ai import AI


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.turn = "X"

    def run(self):
        print("Connect Four — you are X.")
        while True:
            self.board.print()
            if self.turn == "X":
                raw = input("Column (1-7), or q: ").strip().lower()
                if raw == "q":
                    print("Game terminated by player.")
                    return
                try:
                    col_num = int(raw)
                except ValueError:
                    print("Invalid input. Please enter a column number from 1 to 7, or 'q' to quit.")
                    continue

                if not 1 <= col_num <= 7:
                    print("Column out of bounds. Please choose a column between 1 and 7.")
                    continue

                col = col_num - 1
                if self.board.is_col_full(col):
                    print(f"Column {col_num} is full. Please choose another column.")
                    continue
            else:
                col = self.ai.choose_column(self.board)
                if col is None:
                    if self.board.full():
                        self.board.print()
                        print("Game Over: The board is full — it's a draw!")
                        return
                    print("AI cannot make a move.")
                    return

            if self.board.drop(col, self.turn) is None:
                print(f"Column {col + 1} unavailable.")
                continue

            player_name = "Player" if self.turn == "X" else "AI"
            print(f"{player_name} ({self.turn}) placed a disc in column {col + 1}.")

            if self.board.winner(self.turn):
                self.board.print()
                print(f"Game Over: {self.turn} wins!")
                return
            if self.board.full():
                self.board.print()
                print("Game Over: The board is full — it's a draw!")
                return

            self.turn = "O" if self.turn == "X" else "X"

