# line = int(input("Enter the number of lines to print: "))
# character = input("Enter the character to print: ")
# space = line - 1

# for row in range(1, line + 1): #row
#     for numspace in range(space): #space between 
#         print(" ", end="") #space to make it into the pyramid
#     for number in range(1, 2 * row):
#         print(character, end="")
#     space -= 1
#     print()

# print line + 1, if numline %2=0, + 1, if not, do like normal

line = int(input("Enter the number of lines: "))
character = input("Enter the character: ")

space = line - 1

if line %2 ==0:
    linee = line + 1
else:
    linee = line + 0

for row in range(1, int((linee + 2)/2 + 0.5)):
     for numspace in range(space):
         print(" ", end="")
     for number in range(1, 2 * row):
         print(character, end="")
     space -= 1
     print()
    
for row in range(1, int((linee +2)/2 - 0.5)):
    for numspace in range(space):
         print(" ", end="")
    for number in range(1, 2 * row):
         print(character, end="")
    space += 1
    print()