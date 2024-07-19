import random
from Database import data
from art import logo , vs
import os

clear = lambda: os.system('cls')

# To select randomly from data
def select_choice(database):
    rand = random.choice(database)
    # print(rand)
    return rand
    
# To compare if the two choices are the same 
def is_same(choice_A , choice_B):
    if choice_A == choice_B:
        # print("true")
        return True
    else:
        # print("false")
        return False
    
# To compare you answer 
def compare(Choice_A , Choice_B, Player_Answer):
    if Player_Answer == 'a' and Choice_A["follower_count"] > Choice_B["follower_count"]:
        return True
    elif Player_Answer == 'b' and Choice_A["follower_count"] < Choice_B["follower_count"]:
        return True
    else:
        return False
    
def display(choice_A , choice_B):
    print(logo)
    print(f"Score: {score}")
    print(f'Name: {A["name"]}\nDiscription: {A["description"]}\nCountry: {A["country"]}')
    print(vs)
    print(f'Name: {B["name"]}\nDiscription: {B["description"]}\nCountry: {B["country"]}')

score = 0
game_over = False

A = select_choice(database = data)
B = select_choice(database = data)
while is_same(choice_A = A , choice_B = B):
    B = select_choice(database = data)

display(A , B)

while not game_over:
    answer = input("Which one has more follower(A/B): ").lower()

    if compare(A , B, answer):
        score += 1
        if answer == 'b':
            A = B
            B = select_choice(database = data)
        elif answer == 'a':
            B = select_choice(database = data)
            
        while is_same(choice_A = A , choice_B = B):
            B = select_choice(database = data)
        clear()
        display(A , B)
    else:
        clear()
        print(logo)
        print("Incorrect!")
        print(f"Final score: {score}")
        game_over = True
