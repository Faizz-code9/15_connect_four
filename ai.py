import random


class AI:
    def choose_column(self, board, me="O", opponent="X"):
        legal = [c for c in range(7) if not board.is_col_full(c)]
        if not legal:
            return None

        # 1. Take immediate winning move for AI
        for col in legal:
            row = board.drop(col, me)
            if row is not None:
                won = board.winner(me)
                board.grid[row][col] = "."  # Undo simulation
                if won:
                    return col

        # 2. Block opponent's immediate winning move
        for col in legal:
            row = board.drop(col, opponent)
            if row is not None:
                threat = board.winner(opponent)
                board.grid[row][col] = "."  # Undo simulation
                if threat:
                    return col

        # 3. Positional preference: prefer center column if available
        center = 3
        if center in legal:
            return center

        # 4. Fallback: random choice among legal columns
        return random.choice(legal)

