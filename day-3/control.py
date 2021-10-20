#!/usr/bin/env python

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
    print('You said', command)
