"""
This is a program about investment portfolio
It calculates the compound interest over time
with starting amount, rate, and years to hold
the stock value. solved by Pymode-Dev and Question
By Dan Bader
"""

starting_amount = int(input('enter the starting amount: '))
rate_input = int(input('enter the percentage: '))
year_input = int(input('enter the year o hold on to: '))
print(f'starting amount = ${starting_amount:,.2f}, percentage = {rate_input}, year = {year_input}\n')


def invest(start_amount, rate, year):
    for i in range(0, year):   # between the range of 0-year
        initial = start_amount * (rate / 100)   # it calculates the profit rate
        start_amount += initial  # it adds the profit rate to the starting amount
        i += 1
        print(f'year {i}: ${start_amount:,.2f}')


invest(starting_amount, rate_input, year_input)
