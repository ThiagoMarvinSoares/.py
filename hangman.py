word_list = ["ardvack","baboon","camel"]
import random

chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')
display = []
for _ in chosen_word:
    display += '_'

print(display)

guess = input('Guess a letter: ').lower()

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter in guess:
        display[position] = letter

print(display)