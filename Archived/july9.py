# How to print from 2 - 8

# number = 2 (indentify)
# while number < 9: (condition)
#     print (number)
#     number = number + 1 (updating)

# == : equal
# != : equal
# < : smaller
# > : larger

number = int(input("Enter a number: "))
total = 0

while number != 0:
    total += number #total = total + number
    number = int(input("Enter a number: "))

print("Total sum =", total)