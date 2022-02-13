# This is a program about phone and email
# regular expression. By Pymode-Dev

import pyperclip
import re

# this is for phone number
phone_regex = re.compile(r'''(
   (\d{3})|(\(\d{3}\))?              #  area code
   (\s|-|\.)?                        #  separator
   (\d{3})                           #  second number
   (-)                              #  separator
   (\d{4})                           #  third number
)''', re.VERBOSE)
# this is for email addresses
email_regex = re.compile(r'''(
    [a-zA-Z0-9+-._]+                 #  the name format
    @                                # the domain operator
    [a-zA-Z0-9+_.-]+                 # the email addresses provider
    (\.)                             # dot.com
    [a-zA-Z]{1, 3}                   # domain identifier
)''', re.VERBOSE)

text = pyperclip.paste()
container = []
for groups in phone_regex.findall(text):  # finding all phone in the copied text
    phone_num = '-'.join(groups[1], groups[3], groups[5])
    print(phone_num)
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    container.append(phone_num)
for groups in email_regex.findall(text):
    container.append(groups[0])

if len(container) > 0:
    pyperclip.copy('\n'.join(container))
    print('copied to clipboard:')
    print('\n'.join(container))
else:
    print('No phone numbers or email addresses found.')
