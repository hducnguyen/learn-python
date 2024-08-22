# Function for number of rounds
def roundNumber(): 
    while True:
        global rounds
        rounds = int(input("Enter number of rounds, odd numbers only: "))
        if rounds % 2 == 0:
            print("Please re-enter!")
            continue
        else:
            break

# Define a function to display the current state of the board
def display(board_game):
    for i in range(len(board_game)):
        for j in range(len(board_game[i])):
            print(board_game[i][j], end=" ")
        print()


def moveUpdate(playerMoves):
    indexNumber = int(input("Enter your move: "))
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

# Initialize a boolean variable to alternate between X and O moves
move = True
result = []

# Main game loop
roundNumber()
for i in range(rounds):
    board_game = [[], [], []]

    counter = 1
    for i in range(3):
        for j in range(3):
            board_game[i].append(counter)
            counter += 1

    while True:
        if move == True:
            playerMoves = "X"
            move = False
        else:
            playerMoves = "O"
            move = True
        display(board_game)
        moveUpdate(playerMoves)
        if checkForWin(board_game) == True:
            display(board_game)
            print("Winner is " + playerMoves)
            if playerMoves == "X":
                result.append(playerMoves)
            elif playerMoves == "O":
                result.append(playerMoves)
            break

# Displace the grand final result
print(result)        
if result.count('X') > result.count('O'):
    print("Player X wins!")
else:
    print("Player O wins!")
    