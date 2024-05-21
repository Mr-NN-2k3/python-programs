import random
import os

f = open("D:\Computer Programs\Python\database\passwords.txt", "a+")

alpha = ascii(range(0, 127))

password = ''.join(random.choices(alpha, k=8))

f.write(password + '\n')

print(password)
