board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# move = int(input("Enter your move: ")) #assume my move == x

# if move > 0 and move < 10:
#     row = 2 // move
#     col = move % 2
#     print(row, col)
#     board[row][col] = 'x'

# for i in range(len(board)):
#     for j in range(len(board[i])):
#         print(board[i][j], end=" ")
#     print()

for i in range(len(board)): 
    for j in range(len(board[i])):
        print(board[i][j], end=" ")