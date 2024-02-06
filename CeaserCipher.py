alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    def encrypt(text_to, shift_amount):
        cipher = ""
        for i in text:
            position = alphabet.index(i)
            new_position = position + shift
            cipher += alphabet[new_position]
        print(cipher)

    encrypt(text_to=text, shift_amount=shift)
elif direction == 'decode':
    def decrypt(text_to, shift_amount):
        decipher = ""
        for i in text:
            position = alphabet.index(i)
            new_position = position - shift
            decipher += alphabet[new_position]
        print(decipher)

    decrypt(text_to=text, shift_amount=shift)
else:
    print('Invalid input')