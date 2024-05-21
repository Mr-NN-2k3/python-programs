import random
import os
xx = 0
db = open("database\snake_water_gun db.txt", "a+")
#database file location above.
while (xx != 4):

    x = random.choices(["snake", "water", "gun"], k=1)[0]
    xx = input(
        "1.for the snake. \n2.for the water. \n3.for the gun. \n4.exit. \nenter the input for the game :")
    
    if xx == "4":
        print("Exiting the game. Thanks for playing!")
        break
    if xx not in ["1", "2", "3"]:
        print("this is invalid input")
        continue
    #input from the user
    
    if (xx == "1" and x == "water") or (xx == "2" and x == "gun") or (xx == "1" and x == "gun"):
        print("computer wins by having=", x, "human=", xx)
        db.write(
            f"\n\ncomputer WIN by having '{x}'\nwhile human LOST by having '{xx}'")
    #win logic for computer.
    
    elif (xx == "1" and x == "snake") or (xx == "2" and x == "water") or (xx == "3" and x == "gun"):
        print("Human wins the game by having:", xx, "Computer:", x)
        db.write(
            f"\n\ncomputer LOST by having '{x}'\nwhile human WINS by having '{xx}'")
    #win logc for the human.
    else:
        print("its a tie between human and the computer")
        db.write(
            f"\n\nIt was a TIE between the Computer and Human both choose '{x}'")
    #tie logic for the both
