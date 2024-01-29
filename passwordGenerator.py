import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) #4
nr_symbols = int(input(f"How many symbols would you like?\n")) #4
nr_numbers = int(input(f"How many numbers would you like?\n")) #4

#Looping method

password = ''

for lettrs in range(1, nr_letters + 1):
    password += random.choice(letters)

for symbols_ele in range (1, nr_symbols + 1):
    password += random.choice(symbols)

for numbers_ele in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)
#------ Using samble method ------
#random_letters = random.sample(letters, nr_letters)
#random_symbols = random.sample(symbols, nr_symbols)
#random_number = random.sample(numbers, nr_numbers)

#random_letters_string = ''.join(random_letters)
#random_symbols_string = ''.join(random_symbols)
#random_number_string = ''.join(random_number)

#print(random_letters_string + random_symbols_string + random_number_string)