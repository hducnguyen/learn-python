# Initialise board dimension
board_game = [[], [], []]

# Fill the board with numbers as moves for the player
counter = 1
for i in range(3):
    for j in range(3):
        board_game[i].append(counter)
        counter += 1

# Display the board
def display(board_game):
    for i in range(len(board_game)):
        for j in range(len(board_game[i])):
            print(board_game[i][j], end=" ")
        print()

# Update the moves for the players
def moveUpdate(playerMoves):
    indexNumber = int(input("Enter ur move: "))
    for i in range(len(board_game)):
        for j in range(len(board_game[i])):
            if board_game[i][j] == indexNumber:
                board_game[i][j] = playerMoves

def checkForWin(board_game):
    if board_game[0][0] == board_game[0][1] == board_game[0][2]:
        return True
    elif board_game[1][0] == board_game[1][1] == board_game[1][2]:
        return True
    elif board_game[2][0] == board_game[2][1] == board_game[2][2]:
        return True
    elif board_game[0][0] == board_game[1][0] == board_game[2][0]:
        return True
    elif board_game[0][1] == board_game[1][1] == board_game[2][1]:
        return True
    elif board_game[0][2] == board_game[1][2] == board_game[2][2]:
        return True
    elif board_game[0][0] == board_game[1][1] == board_game[2][2]:
        return True
    elif board_game[0][2] == board_game[1][1] == board_game[2][0]:
        return True
        
move = True

while True:
    if move == True:
        playerMoves = "x"
        move = False
    else:
        playerMoves = "o"
        move = True
    display(board_game)
    moveUpdate(playerMoves)
    if checkForWin(board_game) == True:
        print("Winner is " + playerMoves)
        display(board_game)
        break