def is_safe(board, row, col, n):
    # Check if the queen can be placed at board[row][col]

    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check for queens in the upper-left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check for queens in the upper-right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]  # Initialize the chessboard

    def backtrack(row):
        # Base case: All queens are placed successfully
        if row == n:
            return True

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1  # Place the queen

                if backtrack(row + 1):  # Recursive call
                    return True

                board[row][col] = 0  # Backtrack if solution not found

        return False

    if not backtrack(0):
        print(f"No solution exists for n = {n}.")
    else:
        print(f"Solution for n = {n}:")
        for row in board:
            print(" ".join(map(str, row)))


# Taking input from the user
n = int(input("Enter the number of queens (n): "))
solve_n_queens(n)
