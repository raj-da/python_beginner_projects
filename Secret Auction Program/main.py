import os
clear = lambda: os.system('cls')

from art import logo

bid = {}
end = False

while not end:
    print(logo)
    name = input("Name: ")
    amount = float(input("Bid: "))
    bid[name] = amount

    choice = input("Is there any one else(Y/N)").lower()
    if choice == 'n':
        end = True

    clear()

max_bid = 0.0
max_bidder_name = ''
for i in bid:
    if max_bid < bid[i]:
        max_bid = bid[i]
        max_bidder_name = i

print(f"The max bidder is {max_bidder_name} with a bid of {max_bid}")
