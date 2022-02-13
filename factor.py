"""
this is a factor program.
that is finding the factor of a number.
"""

user_input = int(input('enter a positive integer: '))


def factor(number):
    if number <= 0:
        print('enter a positive number')
    else:
        list1 = [i for i in range(1, number + 1) if number % i == 0]
        output = ''.join(f'{i} is a factor of {number}\n' for i in list1)
        print(output)


factor(user_input)
