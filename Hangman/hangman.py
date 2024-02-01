import hangman_words
import hangman_arts
import random
word_list = hangman_words.word_list
stages = hangman_arts.stages
logo = hangman_arts.logo
print(logo)

chosen_word = random.choice(word_list)

#-----------For debugging-----------
#print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in chosen_word:
    display += '_'

word_finished = False
number_of_lives = len(stages) - 1
guessed_letters = []

while not word_finished:
    print(display)
    guess = input('Guess a letter: ').lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter in guess:
            display[position] = letter     
    guessed_letters += guess

    if guess not in chosen_word:
        print(stages[number_of_lives - 1])
        number_of_lives -= 1

    if '_' not in display:
        word_finished = True
        print('Congratulations, you won !')  

    if number_of_lives == 0:
        word_finished = True
        print('Game Over, you are out of lives')  

