import random
from hangman_art import *
from hangman_words import word_list

#to clear the stick man figur every itration 
import os
clear = lambda: os.system('cls')

print(logo)
print("Welcom player")

word = random.choice(word_list)
word_length = len(word)
print("Choosen word:", word)

life = 6
display = []

for i in range(word_length):
    display += "_"

game_over = False

while not game_over:
    guess = input("guess the letter: ")
    clear()
    if guess in display:
        print("You've already gussed this letter!")

    for i in range(word_length):
        if word[i] == guess:
            display[i] = guess
    
    print(' '.join(display)) # to concatinate the list into a single string
    
    if guess not in display:
        print("You've guessed wrong!")
        life -= 1
        if life == 0:
            print("You've lost")
            game_over = True

    if "_" not in display:
        game_over = True
        print("You've won")

    print(stages[life])
