print('Welcome to Treasure Island.\nYour mission is to find the treasure')

step_one = input('Where you want to go to Left or Right?')
step_one_lower = step_one.lower()



if step_one_lower == 'right':
    print('Game over')

step_two = input('Wait or Swim ?')
step_two_lower = step_two.lower()

if step_two_lower == 'wait':
    print('Game over')


step_three = input('You faced three doors, which one you want to open ? Red, Blue or Yellow ?')
step_three_lower = step_three.lower()

if step_three_lower == 'blue':
    print('Congratulations ! You won!')