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

user_input = input('What do you choose ? Type 0 Rock, 1 for Paper or 2 for Scissors\n')
user_input = int()
if user_input == 0:
    print(f'You choose: \n{rock}')
elif user_input == 1:
    print(f'You choose: \n{paper}')
elif user_input == 2:
    print(f'You choose: \n{scissors}')
else:
    print('Invalid input')

random_choice = random.randint(0,2)
if random_choice == 0:
    print(f'The computer chooses: \n{rock}')
elif random_choice == 1:
    print(f'The computer chooses: \n{paper}')
elif random_choice == 2:
    print(f'The computer chooses: \n{scissors}')
else:
    print('Invalid input')

if user_input == 0 and random_choice == 0:
    print('Draw')
elif user_input == 0 and random_choice == 2:
    print('You Win')
elif user_input == 1 and random_choice == 0:
    print('You Win')
elif user_input == 2 and random_choice == 1:
    print('You Win')
else:
    print('Computer Wins!')