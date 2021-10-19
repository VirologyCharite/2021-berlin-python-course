#!/usr/bin/env python

import sys

counts = {}

for line in sys.stdin:
    for word in line.split():
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1

highestCount = -1
mostCommonWord = None

for word, count in counts.items():
    if count > highestCount:
        mostCommonWord = word
        highestCount = count

print('The most common word was', mostCommonWord,
      'which occurred', highestCount, 'times.')
