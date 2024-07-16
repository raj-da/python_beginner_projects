
import os
import random
from art import logo


clear = lambda: os.system('cls')


def get_card(deck):
    """ Takes a list and return a random value"""
    return random.choice(deck)

def calculate_score(hand):
    """Takes a list and add it"""
    score = sum(hand)
    if len(hand) == 2 and score == 21:
        return 0
    if 11 in hand and score > 21:
        score -= 10
    return score

def check_blackjack(score , hand, player_type):
    if score == 0:
        print(f"{player_type} has Blackjack! {player_type} wins!")
        return True
    return False

def determine_winner(player_score , computer_score, player_hand, computer_hand):
    """Determines and prints the winner"""
    clear()
    print(logo)

    if player_score > 21:
        print(f"Your card {player_hand}, current score: {calculate_score(player_hand)} it's a bust")
        print("You've lost")
    elif computer_score > 21:
        print(f"Your card {player_hand}, current score: {calculate_score(player_hand)}")
        print(f"Computer's card{computer_hand}, current score: {calculate_score(computer_hand)} it's a bust")
        print("You've won")
    elif player_score > computer_score:
        print(f"Your card {player_hand}, current score: {calculate_score(player_hand)}")
        print(f"Computer's card{computer_hand}, current score: {calculate_score(computer_hand)}")
        print("You've won")
    elif player_score == computer_score:
        print(f"Your card {player_hand}, current score: {calculate_score(player_hand)}")
        print(f"Computer's card{computer_hand}, current score: {calculate_score(computer_hand)}")
        print("It's a draw")
    else:
        print(f"Your card {player_hand}, current score: {calculate_score(player_hand)}")
        print(f"Computer's card{computer_hand}, current score: {calculate_score(computer_hand)}")
        print("You've lost")

def main():
    end_of_game = False
    while not end_of_game:
        print(logo)
        player = []
        computer = []
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        # Distributing the cards between the player and computer twice 
        for i in range(2):
            player.append(get_card(cards))
            computer.append(get_card(cards))

        player_score = calculate_score(player)
        computer_score = calculate_score(computer)

        print(f"Your card {player}, current score: {player_score}")
        if check_blackjack(player_score , player , "Player"):
            if input("Do you want to play again? ('Y'/'N'): ").lower() == 'n':
                end_of_game = True
            clear()
            continue

        print(f"Computer's first card: {computer[0]} ")
        if check_blackjack(computer_score , computer , "Computer"):
            if input("Do you want to play again? ('Y'/'N'): ").lower() == 'n':
                end_of_game = True
            clear()
            continue
           

        another_card = True
        while another_card and player_score <= 21:
            if input("Type 'y' to get another card and 'n' to stop: ").lower() == 'n':
                another_card = False
                clear()
                print(logo)

            else:
                player.append(get_card(cards))
                player_score = calculate_score(player)
                clear()
                print(logo)
                print(f"Your card {player}, current score: {calculate_score(player)}")
                print(f"Computer's first card: {computer[0]} ")
            

        while calculate_score(computer) < 17:
            computer.append(get_card(cards))
            computer_score = calculate_score(computer)

        determine_winner(player_score , computer_score, player, computer)

        if input("Will you continue the game('Y'/'N'):").lower() == 'n':
            end_of_game = True
        
        clear()

main()
