# score = float(input("Hello, what is your final score? "))

# if score >= 9 and score <= 10:
#     print("Hoc Sinh Xuat Sac")
# elif score >=8 and score < 9:
#     print("Hoc Sinh Gioi")
# elif score >+ 5 and score < 8:
#     print("Hoc Sinh Kha")
# elif score >= 0 and score < 5:
#     print("Duoi TRung Binh")
# else:
#     print("Wrong input, only from 0 to 10 please.")

import time
from typing import ForwardRef
yes_no = ["yes", "no"]

print()                                 
print (" __      __       .__                               ")
print ("/  \    /  \ ____ |  |   ____  ____   _____   ____  ")
print ("\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \ ")
print (" \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ ")
print ("  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >")
print ("       \/       \/          \/            \/     \/")
time.sleep(0.5)
print("")
print("")
print ("  __       ")                  
print ("_/  |_  ___   ")               
print ("\   __\/  _ \ ")                
print (" |  | (  <_> ) ")               
print (" |__|  \____/  ")               
print ("")
time.sleep(0.5)                              
print ("  __  .__      ")               
print ("_/  |_|  |__   ___    ")       
print ("\   __\  |  \_/ __ \  ")       
print (" |  | |   Y  \  ___/  ")      
print (" |__| |___|  /\___  >  ")      
print ("")                           
time.sleep(0.5)                               
print ("   _________    _____   ____  ")
print ("  / ___\__  \  /     \_/ __ \ ")
print (" / /_/  > __ \|  Y Y  \  ___/ ")
print (" \___  (____  /__|_|  /\___  > ")
print ("/_____/     \/      \/     \/ ")
time.sleep(0.5)

name = input("What is your name? ")
print("Great " + name)
while True:
    games = input("Would you want to play the game? ")
    if "yes":
        print("Great " + name + " again. ")
        break
    elif "no":
        print("Oh okk, goodbye" + name)
        quit()
    else:
        print("I don't understand what you said, again please?")
    
path = input("There are 3 paths to go, 1 is left, 2 is right, 3 is straight, which path do you to go? ")

if path == "1":
    print("Okay, you chose to go left. In this path, you have to save a girl name Armelle, okay? ")
    
    print("First thing first, you have to trade with the villagers one things that you think it is good for your journey ")
    
    trading = input("What do you want to trade, 1 is a sword, 2 is a gun and 3 is a spell book? ")
    if trading == "1":
        print("Here is your sword, choose one special ability with it, 1 is fire, 2 is reflection, 3 is ice?  ")
        ability = input("What is your ability, 1, 2, or 3 ")
        if ability == "1":
            print("Okay good, next step, go to the witch and defeat her to get some potion. ")
            print("After 69 days of fighting, you have defeaet the witch")
            
            witch = input("You have just defeat the witch, what potion will you choose, 1 is fire protection, 2 is jump boost, 3 is revive? ")
            if witch == "1":
                print("Good choice, you now have fire protection, it can be use only for once, remember.")
                
                print("Last thing last, you need some protection for your self, head to the blacksmith and but some armor")
                print("There are 3 type of armor, which one will you choose, they all have different special abilities")
                print("1 is made by dragon scales, it can refect fire. 2 is made my Ender Rocks, you can teleport when wearing that. 3 is made by magma rock, it can give you more power")
                armor = input("Which one will you choose, 1, 2, or 3? ")
                if armor == "1":
                    print("Nice, now you are ready to defeat the monster and rescue Armelle")
                    
                    print("You have made the wrong choice, the abilities of the monster is it can control water, you have died because you SUCK, byebye, goodnight. ")
                    print("By the way, you can't rescue Armelle so you SUCK and also NOOB")
                    quit()
                elif armor == "2":
                    print("Nice, now you are ready to defeat the monster and rescue Armelle")
                    
                    print("The monster can control water so that mean your potion is useless, you have to use your armor to get close to the monster.")
                    print("The monster on half health but he use water control right now, you need to dodge, use your armor's power.")
                    print("You nearly defeat it, but you are out of power because dodging too much so you dead <3")
                    print("Bai Bai")
                    quit()
                elif armor == "3":
                    print("Nice, now you are ready to defeat the monster and rescue Armelle")
                    
                    print("The monster can control water so that mean your potion is useless, you have to use your armor increase the damage of your hit.")
                    monster = input("You have to get close to the monster, what would you do, 1 is run into it, 2 is quit, 3 is run into it and then run out.")
                    if monster == "1":
                        print("Nice choice")
                        print("You nearly defeat the monster, but you run into it many times and you start to feel tired so you get killed by the monster")
                        print("Amazing Goodjob 'em")
                    if monster == "2":
                        print("Oh okk")
                        print("Bai bai")
                        quit()
                