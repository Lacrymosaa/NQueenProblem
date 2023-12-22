def print_solution(board):
    for row in board:
        print(" ".join(row))
    print("\n")

def no_collisions(board, row, col, n):
    for i in range(col):
        if board[row][i] == "Q":
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    
    return True

def solve_n_queens_util(board, col, n, solutions):
    if col == n:
        solutions.append([row[:] for row in board])
        return

    for i in range(n):
        if no_collisions(board, i, col, n):
            board[i][col] = "Q"
            solve_n_queens_util(board, col + 1, n, solutions)
            board[i][col] = "."

def solve_n_queens(n):
    solutions = []
    board = [["." for _ in range(n)] for _ in range(n)]
    solve_n_queens_util(board, 0, n, solutions)
    return solutions

# Determine o valor de N dentro da chamada de solve_n_queens
solutions_n_queens = solve_n_queens(8)
i = 1
for solution in solutions_n_queens:
    print(f"Solução n° {i}")
    print_solution(solution)
    i += 1
