#!/usr/bin/env python

from time import sleep

command = 'whatever'

# while command != 'quit':
# or...
# while not (command == 'quit'):
#     command = input('what is your command? ')
#     print('You said', command)


while True:
    command = input('what is your command? ')
    if command == 'quit':
        break
    elif command == 'sleep':
        sleep(3)
    elif command == 'eat':
        print('yum')
    else:
        print('You said', command)
