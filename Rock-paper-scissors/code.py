rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

alternatives = [rock , paper, scissors]

computer_choice = random.randint(0 , 2)


print("Choose 0 for rock, 1 for paper, 2 for scissors")
user_choice = int(input("Choice: "))

print(alternatives[user_choice])
print("Computer Choice: \n" + alternatives[computer_choice])


if user_choice == 0:
    match computer_choice:
        case 0:
            print("Draw")
        case 1:
            print("You lose")
        case 2:
            print("You win")
elif user_choice == 1:
    match computer_choice:
        case 0:
            print("You win")
        case 1:
            print("Draw")
        case 2:
            print("You lose")
else:
    match computer_choice:
        case 0:
            print("You lose")
        case 1:
            print("You win")
        case 2:
            print("Draw")
