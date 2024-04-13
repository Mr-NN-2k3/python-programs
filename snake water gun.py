import random
xx = 0
while (xx != 4):

    x = random.choices(["snake", "water", "gun"], k=1)[0]
    xx = input('''1.for the snake
               2.for the water
               3.for the gun 
               4.exit
               enter the input for the game :''')
    if xx == "4":
        print("Exiting the game. Thanks for playing!")
        break
    if xx not in ["1" , "2", "3"]:
        print("this is invalid input")
        continue

    if (xx == "1" and x == "water") or (xx == "2" and x == "gun") or (xx == "1" and x == "gun"):
        print("computer wins by having=", x, "human=", xx)
    elif (xx == "1" and x == "snake") or (xx == "2" and x == "water") or (xx == "3" and x == "gun"):

        print("Human wins the game by having:", xx, "Computer:", x)
    else:
        print("its a draw")
