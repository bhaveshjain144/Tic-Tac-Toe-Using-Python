import random

# Function to print the tic-tac-toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

# Function for the computer's move (AI)
def computer_move(board, computer, player):
    # Check for a winning move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = computer
                if check_winner(board, computer):
                    return

                board[i][j] = " "

    # Check for a blocking move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player
                if check_winner(board, player):
                    board[i][j] = computer
                    return
                board[i][j] = " "

    # Try to take a corner
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    random.shuffle(corners)
    for i, j in corners:
        if board[i][j] == " ":
            board[i][j] = computer
            return

    # Try to take the center
    if board[1][1] == " ":
        board[1][1] = computer
        return

    # Take any available side
    sides = [(0, 1), (1, 0), (1, 2), (2, 1)]
    random.shuffle(sides)
    for i, j in sides:
        if board[i][j] == " ":
            board[i][j] = computer
            return

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    computer = "O"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        if player == "X":
            row, col = map(int, input("Enter row and column (e.g., 1 2): ").split())
            if board[row - 1][col - 1] != " ":
                print("That spot is already taken. Try again.")
                continue
        else:
            computer_move(board, computer, player)

        board[row - 1][col - 1] = player
        print_board(board)

        if check_winner(board, player):
            print(f"{player} wins! Congratulations!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        player, computer = computer, player

# Start the game
if __name__ == "__main__":
    play_game()
