import random

while True:
    x = random.choice(["snake", "water", "gun"])
    xx = input('''1. For snake
2. For water
3. For gun 
4. Exit
Enter your choice: ''')

    if xx == "4":
        print("Exiting the game. Thanks for playing!")
        break
    elif xx not in ["1", "2", "3"]:
        print("Invalid input, please try again.")
        continue
    elif xx == "1":
        xx = "snake"
    elif xx == "2":
        xx = "water"
    elif xx == "3":
        xx = "gun"

    if (xx == "snake" and x == "water") or (xx == "water" and x == "gun") or (xx == "gun" and x == "snake"):
        print("\nComputer wins. You chose:", xx, "\nComputer chose:", x , "\n\n\n")
    elif (xx == "snake" and x == "snake") or (xx == "water" and x == "water") or (xx == "gun" and x == "gun"):
        print("\nYou win! You chose:", xx, "\nComputer chose:", x, "\n\n\n")
    else:
        print("\nIt's a draw! You both chose:", xx , "\n\n\n")
