import random

x = range(1 , 10)
i = 0

var = random.sample(x , k = 1)

for var in range(i):
    input1 = int(input("enter your guess => "))
    if input1 == var:
        print("you won the game.")
        break
        i+=1
        
    if i==3:
        print("plz try again you have used " , i , "no of chances from 3 ")

else:
    print("you lost the game")


