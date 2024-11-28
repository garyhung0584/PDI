def is_valid(board, row, col, num):
    block_row, block_col = 2 * (row // 2), 2 * (col // 2)

    if num in board[row] or num in [board[i][col] for i in range(4)]:
        return False
    for i in range(2):
        for j in range(2):
            if board[block_row + i][block_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                for num in range(1, 5):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    board = []
    for _ in range(4):
        board.append(list(map(int, input().split())))

    if solve_sudoku(board):
        print_board(board)
    else:
        print("No solution exists.")
