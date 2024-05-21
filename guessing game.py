import random
import os

f = open("D:\Computer Programs\Python\database\guessing_gamedb.txt", "a+")
#input your desired file location above.

var = random.choice(range(0, 10))
i = 0
play = int(input(
    "To play the game press => 1\nTo exit the game press => 2\nYour selection = "))
while (play == 1):
    for x in range(3):

        input1 = int(input("enter your guess => "))

        if input1 == var:
            f.write("win"+"\n")
            print("you won the game.")
            break
        # Winning logic here
        
        i = i+1
        if i <= 2:
            print("plz try again you have used ", i, "no of chances from 3 ")
        #Number of the chances to display.
        else:
            print("\n\nyou lost the game. \nThe correct number was  ", var)
            f.write("lost" + "\n")
        #losing logic here.

print("Exiting the game.\nSee You Again")
#the exiting the game logic.
