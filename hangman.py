word_list = ["ardvack","baboon","camel"]
import random

chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')
display = []
for _ in chosen_word:
    display += '_'

word_finished = False
number_of_lives = 6

while not word_finished:
    print(display)
    guess = input('Guess a letter: ').lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter in guess:
            display[position] = letter

    if guess not in chosen_word:
        number_of_lives -= 1
        print(f'You have {number_of_lives} lives left.')

    if '_' not in display:
        word_finished = True
        print('Congratulations, you won !')

    if number_of_lives == 0:
        word_finished = True
        print('Game Over, you are out of lives')  
