import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text_to, shift_amount,direction_swith):
        cipher = ""
        for i in text:
            position = alphabet.index(i)
            if direction_swith == 'encode':
                new_position_cipher = position + shift
                cipher += alphabet[new_position_cipher]
            elif direction_swith == 'decode':
                new_position_cipher = position - shift
                cipher += alphabet[new_position_cipher]
        print(cipher)   

encrypt(text_to=text, shift_amount=shift, direction_swith=direction)