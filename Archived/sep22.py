#1) Write a program that allows the user to enter a number from 1-12, display the month in English
# Example:
#     Input: Enter month in number: 12
#     Output: December

# from typing import type_check_only


# number = int(input("Enter month in number: "))

# if number == 1:
#     print("January")
# elif number == 2:
#     print("February")
# elif number == 3:
#     print("March")
# elif number == 4:
#     print("April")
# elif number == 5:
#     print("May")
# elif number == 6:
#     print("June")
# elif number == 7:
#     print("July")
# elif number == 8:
#     print("August")
# elif number == 9:
#     print("September")
# elif number == 10:
#     print("October")
# elif number == 11:
#     print("November")
# elif number == 12:
#     print("December")
# else:
#     print("invalid input")

#2) Write a program that allows the user to enter a number for temperature and a degree in Celsius (C) or Fahrenheit (F). Perform the conversion between them
# Example:
#     Input:
#         Enter temperature: 30
#         Enter degree: C
#     Output:
#         30 C = 86 F

# degree = float(input("Enter temperature: "))
# typeof = input("Enter the degree type: ")

# fromctof = degree * 1.8 + 32
# fromftoc = degree - 32 * 5/9

# if typeof == "C":
#     print(str(degree) + " C" + " = " + str(fromctof) + " F")
# elif typeof == "F":
#     print(str(degree) + " F" + " = " + str(fromftoc) + " C")
# else:
#     print("Invalid input")

# 3) Write a program that asks user to enter username and password. If they can enter correct username and password within 5 attempts, allow them to login. If they try to login more than 5 times, lock the account
# Example:
#     Enter your username: ...
#     Enter your password: ...
    
#     if username and password are correct: login successfully
#     if failed: your account has been locked

username = "hducng"
password = "hduckhongaihotve"

askforname = input("Enter your username: ")
askforpass = input("Enter your password: ")

for tries in range(4,-1, -1):
    if askforname == "hducng" and askforpass == "hduckhongaihotve":
        print("Login succesfully")
        break
    elif askforname == "hducng" and askforpass != "hduckhongaihotve":
        print("Wrong password, " + str(tries) + "tries left")
        askforname = input("Enter your username: ")
        askforpass = input("Enter your password: ")
    else:
        print("Unable to find your account, " + str(tries) + "tries left")
        askforname = input("Enter your username: ")
        askforpass = input("Enter your password: ")

    if tries == 1:
        print("YoUr AcCoUnT hAs BeEn LoCkeD")
        break