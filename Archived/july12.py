# print number triangle

# line = int(input("Enter how many lines to print: "))

# for row in range(1, line + 1):
#     for number in range(1, row + 1):
#         if number < 10:
#             print("0" + str(number), end=" ")
#         else: 
#             print(number, end=" ")
#     print()

# HW: Print the character pyramid

line = int(input("Enter the number of lines to print: "))
character = input("Enter the character to print: ")
space = line - 1

for row in range(1, line+1): #for the row
    for numspace in range(space): #space between
        print(" ", end="")
    for number in range(1, 2*row):
        print(character, end="")
    space -= 1
    print()