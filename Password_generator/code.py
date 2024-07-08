# This version assums no user input error
# Will be improven 
from os import name
import random
import string
# To change the string into a list
characters = list(string.ascii_letters + string.digits + string.punctuation)
random.shuffle(characters)

num = int(input("Enter length of password: "))
print("your password: ", end='')
for i in range(0 , num):
    print(characters[random.randint(0 , len(characters) - 1)] , end='')
