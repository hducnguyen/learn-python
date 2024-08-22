#listname = ["stuff1, stuff2, ..."]
 
#  Insert an item at any position inside the list
# list.insert(position, "thing that we want to add")

# remove an item by name
# list.remove("Name")

# reverse a list
# list.reverse()

# remove an item at the end
# list.pop(index)

# remove item by its position
# del list[numberofthingthatwewanttodel]

# len(nameofthelist)

# import random # a python duilt-in module

# print(random.randint(10, 20)) random number from 10 - 20 include 10 and 20

import random

moves = ["rock", "paper", "scissors",]

scores = 0

while True:
    random_number = random.randint(0, len(moves) - 1)
    comp_moves = moves[random_number]

    player_move = input("Enter your move: ")
    print("Computer move: ", comp_moves)

    if player_move == 'rock':
        if comp_moves == moves[0]:
            print("Draw")
        elif comp_moves == moves[1]:
            print("Computer wins, you suck :v")
            scores -= 1
        elif comp_moves == moves[2]:
            print("You win, luckily...")
            scores += 1

    if player_move == 'paper':
        if comp_moves == moves[0]:
            print("You win, luckily...")
            scores += 1
        elif comp_moves == moves[1]:
            print("Draw")
        elif comp_moves == moves[2]:
            print("Computer wins, you suck :v")
            scores -= 1

    if player_move == 'scissors':
        if comp_moves == moves[0]:
            print("Computer wins, you suck :v")
            scores -= 1
        elif comp_moves == moves[1]:
            print("You win, luckily...")
            scores += 1
        elif comp_moves == moves[2]:
            print("Draw")

    if player_move == 'suckers':
        print("You are stupid")

    if player_move == 'quit':
        print("Get out of here")
        break
    
    if player_move == 'Hacking':
        print("No, you are stupid")

    print('Scores: ' + str(scores))