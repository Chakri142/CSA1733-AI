import math

def print_board(board):
    for row in board:
        print("|".join(row))
    print()

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth+1, False))
                    board[i][j] = ' '
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth+1, True))
                    board[i][j] = ' '
        return best

def best_move(board):
    best_score = -math.inf
    move = (0, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

board = [[' ' for _ in range(3)] for _ in range(3)]

while True:
    print_board(board)
    row = int(input("Enter your move row (0-2): "))
    col = int(input("Enter your move col (0-2): "))
    if board[row][col] == ' ':
        board[row][col] = "X"
        if check_winner(board) == "X":
            print_board(board)
            print("You win!")
            break
        if is_full(board):
            print_board(board)
            print("Draw!")
            break

        ai_row, ai_col = best_move(board)
        board[ai_row][ai_col] = "O"
        if check_winner(board) == "O":
            print_board(board)
            print("AI wins!")
            break
        if is_full(board):
            print_board(board)
            print("Draw!")
            break
    else:
        print("Invalid move!")
