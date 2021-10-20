#!/usr/bin/env python

def sequenceMatch(sequence, pattern):
    if pattern in sequence:
        print('yes')
    else:
        print('no')


sequenceMatch('ACGGTCAAAC', 'AAA')
sequenceMatch('ACGGTCAAAC', 'XXX')
