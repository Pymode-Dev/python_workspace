import random


messages = ['it is certain', 
            'it is decidedly so', 
            'yes definitely',
            'reply hazy',
            'ask again later',
            'concentrate and ask again',
            'my reply is no',
            'outlook not so good',
            'very doubtful']

print(messages[random.randint(0, len(messages)-1)])
