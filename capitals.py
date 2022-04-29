"""
This is a program that asks the user a question about
state and capital  until the user get the answer.
"""

import random

CAPITALS_DICT = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahasse',
    'Georgia': 'Atlanta'
}

STATES = [state for state in CAPITALS_DICT]
CAPITALS = [capital for capital in CAPITALS_DICT.values()]
RANDOM_QUESTION = random.choice(STATES)

while True:
    print('If you want to quit, just press q. ')
    ASK_USER = input(f"What is the capital of {RANDOM_QUESTION}: ")
    if ASK_USER.title() == CAPITALS_DICT[RANDOM_QUESTION]:
        print("Correct answer")
        break
    elif ASK_USER.lower() == 'q':
        print('Goodbye!!!')
        print(f"The capital of {RANDOM_QUESTION} is --> \
              {CAPITALS_DICT[RANDOM_QUESTION]}")
        break
    else:
        print("Incorrect answer, try again!!!")

      