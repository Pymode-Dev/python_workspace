birthdays = {'seun': 'apr 1', 'bolu': 'dec 5', 'jeremiah': 'jan 12', 'joseph': 'nov 17'}

print('enter a name (type q to quit): ')
while True:
    name = input()
    if name == ' ':   # when the if statement is true, it breaks
        break
    # when it breaks, it will stop here.
    if name in birthdays:   # when the user input is present in the database
        print(birthdays[name] + ' is the birthday of ' + name)
    else:   # if not there
        print(f'I do not have {name} birthday')
        print(f'What is {name} birthday? ')
        birthday = input()   # it asks for the birthday of the person absent
        birthdays[name] = birthday   # and it updated it into the database
    print('Database updated')    
            