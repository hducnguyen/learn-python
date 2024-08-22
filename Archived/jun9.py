





# # # # # name = input("What is your name? ")
# # # # # print('hello ' + name)

# # # # # Data types:
# # # # #     1. String: characters => Hoang Brian Duc password123@
# # # # #         need to be wrapped around a single quote or double quote: "Duc" , 'Hoang'











































































































































































3322222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222# # # # #     2. Integers: whole numbers => 1, 5, , -5, 0
# # # # #     3. Float (floating point): decimal numbers => 3.14, 1.234
# # # # #     4. Boolean: True/False

# # # # # name = 'Jack'
# # # # # age = 25

# # # # a = 5
# # # # b = 10
# # # # print(a + b) => 15

# # # # a = '5'
# # # # b = '10'
# # # # print(a + b) => 510

# # # # Data type consistency: str + int,  int + bool, str + float => impossible operation!

# # # # Ex: age calculator
# # # #     1. When were you born: 2008
# # # #     => Your are 13 years old

# # # # Type casting: convert one type to another
# # # # Int => str:
# # # #     int(age)
# # # # Str => int: str(number_a)

# # # # name = "Jack"
# # # # int(name)

# # # # year = "1995"

# # # # int(year)

# # # # birthyear = int(input("When were you born? "))
# # # # thisyear = 2021
# # # # age = thisyear - birthyear
# # # # print("You are " + str(age) + " years old ")

# # # # Ex: simple calculator
# # # # - Enter number a: 5
# # # # - Enter number b: 9
# # # # Give four outcomes: + - * /

numA = float(input("What is your first number? "))
numB = float(input("What is your second number? "))
sum = numA + numB
difference = numA - numB
product = numA * numB
division = numA/numB

print(str(numA) + " + " + str(numB) + " = " + str(sum))
print(str(numA) + " - " + str(numB) + " = " + str(difference))
print(str(numA) + " * " + str(numB) + " = " + str(product))
print(str(numA) + " / " + str(numB) + " = " + str(division))

# # Control flow

# # Condition: if-elif-else

# # if rain == True:
# #     print("Take an umbrella")
# # else:
# #     # print("Go play outside")
# # elif

# HW: Buila a small Siri:
#     1. Ask for their name and gender: male/female/other
#     2. ASk where the user from: USA, VN, ...
#     3. Say hello in that language: Xin chao, Hello, ... multiple languages

# name = input("What is your name? ")
# gender = input("What is your gender, male/female/others? ")
# country = input("Where are your from? ") 

# if gender == "male": 
#     title = "Mr."
# elif gender == "female":
#     title = "Ms."
# elif gender == "others":
#     title = ""
    
# if country == "Vietnam":
#     greeting = "Xin chao"
# elif country == "USA":
#     greeting = "Hello"
# elif country == "China":
#     greeting = "你好"
# else:
#     greeting = "Hello"

# print(greeting  + " " + title + " " + name)