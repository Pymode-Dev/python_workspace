"""
This program select randomly a state and ask for the capital.
And it checks if the user is correct.
"""
import random

capitals_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta'
}

# To loop through the dictionary and get the state randomly
states = []
capitals = []
for k, v in capitals_dict.items():
    states += [k]   # it created a list of state
    capitals += [v]   # it created a list of capitals
random_state = random.choice(states)   # this chooses randomly from states
answer = capitals_dict[random_state]   # the state chooses randomly will be called
# to get the value from the main dictionary

# This is the quiz module
while True:
    print(f'What is the capital of {random_state}? ')
    user_input = input().title()
    if user_input == answer:
        print('You got the answer!!!')
        break
    else:
        print('incorrect answer :(')
        user_input = input('Do you want to quit (by pressing q) or press no to continue? ')
        if user_input != 'q':   # if the user input is not equal to q
            # it continues the loop
            print('Ok, continue...')
        elif user_input == 'q':
            print(f'The answer is: {answer} \nGoodbye!!!')
            break
