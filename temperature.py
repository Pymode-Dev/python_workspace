"""
This is temperature converter program
from celsius to fahrenheit in def1
from fahrenheit to celsius in def2
"""

user_input = float(input('Enter a temperature in degrees C: '))


def cel_to_far(celsius):
    f = celsius * 9/5 + 32
    print(f'{user_input} degrees C = {f:.2f} degrees F')


cel_to_far(user_input)

user_input = float(input('Enter a temperature in degrees C: '))


def far_to_cel(far):
    c = (far - 32) * 5/9
    print(f'{user_input} degrees F = {c:.2f} degrees C')


far_to_cel(user_input)
