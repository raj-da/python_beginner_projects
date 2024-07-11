from art import logo
import string

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(our_word , shift , choice):
    if choice == "e":
    
        for i in range(len(our_word)):
            if our_word[i] in string.ascii_lowercase:
                index = alphabet.index(our_word[i])
                new_index = index + shift
                if new_index > 25:
                    new_index %=  26
                word[i] = alphabet[new_index]
            else:
                word[i] = our_word[i]
        
        text = "".join(word)
        print(f"The encoded text is {text}")

    if choice == "d":

        for i in range(len(our_word)):
            if our_word[i] in string.ascii_lowercase:
                index = alphabet.index(our_word[i])
                new_index = index - shift
                word[i] = alphabet[new_index]
            else:
                word[i] = our_word[i]

        text = "".join(word)

        print("Decrypted messege:", text)

stop = False
while not stop:
        
    direction = input("Type 'e' to encrypt, type 'd' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift_size = int(input("Type the shift number: "))
    word = []
    for i in range(len(text)):
        word.append(text[i])
    caesar(our_word = word , shift = shift_size, choice = direction)

    stop = input("Would you like to continue the program(Y/N): ").lower()
    if(stop == 'n'):
        stop = True
    else:
        stop = False
