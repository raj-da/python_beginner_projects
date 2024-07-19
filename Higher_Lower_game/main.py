import random
from Database import data
from art import logo , vs
import os

clear = lambda: os.system('cls')

# To select randomly from data
def select_choice(database):
    rand = random.choice(database)
    return rand
    
# To compare if the two choices are the same 
def is_same(choice_A , choice_B):
    return choice_A == choice_B
    
# To compare you answer 
def compare(Choice_A , Choice_B, Player_Answer):
    if Player_Answer == 'a':
        return Choice_A["follower_count"] > Choice_B["follower_count"]
    elif Player_Answer == 'b':
        return Choice_A["follower_count"] < Choice_B["follower_count"]
    return False
    
def display(choice_A , choice_B, score):
    print(logo)
    print(f"Score: {score}")
    print(f'Name: {choice_A["name"]}\nDiscription: {choice_A["description"]}\nCountry: {choice_A["country"]}')
    print(vs)
    print(f'Name: {choice_B["name"]}\nDiscription: {choice_B["description"]}\nCountry: {choice_B["country"]}')

def main():
    score = 0
    game_over = False

    A = select_choice(database = data)
    B = select_choice(database = data)
    while is_same(choice_A = A , choice_B = B):
        B = select_choice(database = data)

    display(A , B, score)

    while not game_over:
        answer = input("Which one has more follower(A/B): ").lower()
        if answer not in ['a' , 'b']:
            print("Invalid input. Please enter 'A' or 'B'.")
            continue

        if compare(A , B, answer):
            score += 1
            if answer == 'b':
                A = B
            B = select_choice(database = data)
            while is_same(choice_A = A , choice_B = B):
                B = select_choice(database = data)
            clear()
            display(A , B, score)
        else:
            clear()
            print(logo)
            print("Incorrect!")
            print(f"Final score: {score}")
            game_over = True

main()



