# 1. Multiplication table:
#     What do you want to do, enter 1 for a particular number, enter 2 for the full table
#     a. Accept a number, print the mul. table of that number
#         ex number = 6: 6 12 18 24 30 36 42 ... 60
#     b. Print the full mul. table from 1 to 10

# function = int(input("Choose 1 or 2, 1 is one specific multiplication table, 2 is all multiplication tale from 1-10? "))
# if function == 1:
#     number = int(input("Enter one number: "))
#     for i in range(1, 11):
#         product = number * i
#         print(product, end=" ")
# else:

# 2. Print even or odd numbers within a range
#     - Starting number: 3
#     - Stopping number: 20
#     - Even or odd numbers: odd
#     -> 3 5 7 9 11 13 15 17 19

#     - Starting number: 2
#     - Stopping number: 69
#     - Even or odd numbers: even
#     -> 2 4 6 ... 68

#     - Starting number: 2    
#     - Stopping number: 69
#     - Even or odd numbers: odd
#     -> 3 5 7 9 ... 69

# startnumber = int(input("What is the starting number? "))
# endnum = int(input("What is the ending number? "))
# typeofnum = input("What type of number do you want to print? ")

# for i in range(startnumber, endnum + 1, 2):
#     if typeofnum == "odd":
#         print
#     elif typeofnum == "even":
#         print

# startnumber = int(input("What is the starting number? "))
# endnum = int(input("What is the ending number? "))

# if endnum < startnumber:
#     difference = -1
#     endnum = endnum -1
# else:
#     difference = 1
#     endnum = endnum + 1

# for i in range(startnumber, endnum, difference):
#     print(i)  

startnum = int(input("What is the starting number? "))
endnum = int(input("What is the ending number "))
typeofnum = input("What type of number that you want to print? ")

if endnum > startnum:
    difference = 2
    if typeofnum == "even":
        if startnum % 2 == 1:
            startnum = startnum + 1
            endnum = endnum + 1
    elif typeofnum == "odd":
        if startnum % 2 == 0:
            startnum = startnum + 1
            endnum = endnum + 1
    else:   
        print("Sorry I don't understand. ")
        quit()
elif endnum < startnum:
    difference = - 2
    if typeofnum == "even":
        if startnum % 2 == 1:
            startnum = startnum - 1
            endnum = endnum - 1
    elif typeofnum == "odd":
        if startnum % 2 == 0:
            startnum = startnum -1
            endnum = endnum -1
    else:   
        print("Sorry I don't understand. ")
        quit()

for i in range(startnum, endnum + 1, difference):
    print(i)