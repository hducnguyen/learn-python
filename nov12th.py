# Display a number for 1s, then it will clear the screen
    
# 2

# ...

# 2

# 2 3

# ... Enter numbers: 2 3

# 2 3 9

# ... : 2 3 9
# 2 3 9

# ...

import os
import time
import random

# while True:
#     print('hi')
#     time.sleep(1)
#     os.system('cls')
#     print('after clear')
#     time.sleep(1)
#     os.system('cls')


numbers = []
process = True
while process:
    ranNum = random.randint(0, 9)
    numbers.append(ranNum)
    print(numbers)
    time.sleep(1)
    os.system('cls')
    userAns = (input("\nEnter numbers: ")).split(' ')

    for i in range(len(userAns)):
        userAns[i] = int(userAns[i])

    for i in range(len(numbers)):
        if userAns[i] != numbers[i]:
            process = False

print(numbers)
print("Game over")