#!/usr/bin/env python

import sys

from Bio import SeqIO

def sequenceMatch(records, pattern):
    for record in records:
        if pattern in record.seq:
            print(record.description, 'yes')
        else:
            print(record.description, 'no')

pattern = input('Enter a pattern: ')
# if pattern = 'quit':

records = []

with open(sys.argv[1]) as fp:
    for record in SeqIO.parse(fp, 'fasta'):
        records.append(record)

print(f'Read {len(records)} FASTA sequences from {sys.argv[1]!r}')
sequenceMatch(records, pattern)
