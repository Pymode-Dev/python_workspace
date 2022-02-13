#! /usr/bin/python3

import random

connector = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
password = ''.join(random.choice(connector) for i in range(21))
print(password)
