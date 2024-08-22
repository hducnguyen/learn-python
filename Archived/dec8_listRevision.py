countries = ['america', 'malaysia', 'singapore', 'philipines', 'china', 'taiwan']

# print("I have been to " + str(len(countries)) + " countries.")
# HW
# 1.
# print("1. " + "There are " + str(len(countries)) + " countries.")
# 2.
# print("2. " + countries[2] + " is next to " + countries[1])
# 3.
# print("I have been to: ")
# for i in range(len(countries)):
#     print("- " + countries[i])
#     i + 1
# 4

country = input("What country have you been to? ")

# if country == countries[0]:
#     print("I have also been to " + countries[0] +  ". It's a beautiful country!")
# elif country == countries[1]:
#     print("I have also been to " + countries[1] +  ". It's a beautiful country!")
# elif country == countries[2]:
#     print("I have also been to " + countries[2] +  ". It's a beautiful country!")
# elif country == countries[3]:
#     print("I have also been to " + countries[3] +  ". It's a beautiful country!")
# elif country == countries[4]:
#     print("I have also been to " + countries[4] +  ". It's a beautiful country!")
# elif country == countries[5]:
#     print("I have also been to " + countries[5] +  ". It's a beautiful country!")
# else:
#     print("I would like to go to " + country + " someday.")
countryFound = False
for i in range(len(countries)):
    if country == countries[i]:
        print("I have also been to " + countries[i] +  ". It's a beautiful country!")
        countryFound = True
        break
if countryFound == False:
    print("I'd love to travel to " + country + " someday")
