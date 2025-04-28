# Initialize board dimension
board_game = [[], [], []]

# Fill the board with numbers as moves for the player
counter = 1
for i in range(3):
    for j in range(3):
        board_game[i].append(counter)
        counter += 1

# Display the board
def display(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()

# Custom procedure with parameters to update the board
def move_update(board, player_symbol) -> bool:
    move_number = int(input("Enter your move (1-9): "))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == move_number:
                board[i][j] = player_symbol
                return True  # Return True when a move is successfully made
    print("Invalid move. Try again.")
    return False  # Return False if move is invalid

# Check if the current board has a winner
def check_for_win(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return True
        elif board[0][i] == board[1][i] == board[2][i]:
            return True
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] == board[1][1] == board[2][0]:
        return True
    return False

# Main game loop
current_player = "X"
while True:
    display(board_game)
    successful_move = move_update(board_game, current_player)
    if successful_move:
        if check_for_win(board_game):
            print("Winner is " + current_player)
            display(board_game)
            break
        # Switch player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"