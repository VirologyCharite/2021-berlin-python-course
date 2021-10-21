#!/usr/bin/env python

import argparse
from Bio import SeqIO

# import sys
# print('The command line is', sys.argv)


parser = argparse.ArgumentParser(
    description='Demonstrate the use of argparse.')

parser.add_argument(
    '--file',
    help='The FASTA file to look in.')

parser.add_argument(
    '--pattern', required=True,
    help='The pattern to look for.')

parser.add_argument(
    '--maxLength', '-n', type=int, default=10,
    help='The maximum pattern length.')

parser.add_argument(
    '--maxErrors', type=int, default=10,
    help='The maximum number of errors.')


args = parser.parse_args()

print(f'The file is {args.file!r}.')
print(f'The pattern is {args.pattern!r}.')
print(f'The max pattern length is {args.maxLength}.')

records = []

with open(args.file) as fp:
    for record in SeqIO.parse(fp, 'fasta'):
        records.append(record)

# Here's how we used to have to write the above:
# fp = open(args.file)
# for record in SeqIO.parse(fp, 'fasta'):
#    records.append(record)
# fp.close()

print(f'Read {len(records)} sequences from {args.file!r}.')

for record in records:
    if len(record) > args.maxLength:
        print(f'Sequence {record.id!r} has length {len(record)} '
              f'which is > {args.maxLength}')

for record in records:
    if args.pattern in record.seq:
        print(f'Sequence {record.id!r} matches {args.pattern!r}')
