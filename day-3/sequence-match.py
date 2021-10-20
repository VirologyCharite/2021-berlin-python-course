#!/usr/bin/env python

def sequenceMatch(sequence, pattern):
    if pattern in sequence:
        print('yes')
    else:
        print('no')


while True:
    sequence = input('Enter a sequence: ')
    if sequence == 'quit':
        break

    pattern = input('Enter a pattern: ')

    sequenceMatch(sequence, pattern)
