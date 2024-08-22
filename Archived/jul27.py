# BIDV bank - 5.6 interest for a year

# 1st year:
# Deposit Money: 1,000,000
# Increase: 1,000,000 * 0.056 =56,000
# After a year, the money will increase to 1,056,000

# 2nd year: reuse the money  from the previous year
# Deposit Money: 1,056,000
# Increase: 1,056,000 * 0.056 =59,136
# After a year, the money will increase to 1,115,136

# ...

# Write a program that allows the user to enter:
#     1. Deposit money from the start (for simplicity, ignote the last three zero)
#     2. yearrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
#     Show that total money year

money = float(input("What is your amount of deposit money? "))
years = int(input("How many years do you want to keep it? "))
interestR8 = 0.056

for i in range(1,years + 1):
    outcome = money * interestR8
    money = outcome + money
    print("This is the money for the year number " + str(i) + ": " + str(money))