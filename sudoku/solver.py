# solver.py
def solve(board):
    """
    Solves the Sudoku puzzle using backtracking.
    :param board: 2D list representing the Sudoku board (9x9 grid).
                  Empty cells are represented by 0.
    :return: True if a solution exists, False otherwise.
    """
    def is_valid(board, row, col, num):
        """
        Checks if placing `num` at `board[row][col]` is valid.
        """
        # Check row
        if num in board[row]:
            return False
        
        # Check column
        if num in [board[i][col] for i in range(9)]:
            return False
        
        # Check 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        
        return True

    def backtrack():
        """
        Backtracking algorithm to solve the Sudoku puzzle.
        """
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:  # Empty cell
                    for num in range(1, 10):  # Numbers 1-9
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if backtrack():
                                return True
                            board[row][col] = 0  # Undo move
                    return False  # No valid number found
        return True  # Puzzle solved

    return backtrack()
