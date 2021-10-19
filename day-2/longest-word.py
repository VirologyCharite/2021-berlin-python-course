#!/usr/bin/env python

import sys

words = set()

NONWORDS = {
    '(trademark/copyright)',
    '(www.gutenberg.org)',
}

for line in sys.stdin:
    line = line.replace('-', ' ').replace(',', ' ').replace('.', ' ')
    for word in line.split():
        if (word.startswith('http') or word.startswith('www.')
                or word in NONWORDS):
            continue
        words.add(word)

maxLength = -1
longestWord = None

for word in words:
    if len(word) > maxLength:
        longestWord = word
        maxLength = len(word)

print('The longest word was', longestWord,
      'with length', maxLength, 'letters.')
