# Password Checker

entered_username = "jack"
entered_password = "jackissingle"

entering_username = input("What is your username? ")
entering_password = input("What is your password? ")

for tries in range(5):
    if entering_username == entered_username and entering_password == entered_password:
        print("Login succesful")
        break
    else:
        print("Try agian pls, 4 tries left. ")
        