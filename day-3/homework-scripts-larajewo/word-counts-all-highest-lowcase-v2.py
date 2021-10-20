#!/usr/bin/env python

import sys

counts = {}

for line in sys.stdin:
    for word in line.split(): #or for word in line.lower().split(): (single line instead 12+13)
        low = word.lower()

        if low in counts:
            counts[low] = counts[low] + 1 #or counts[low] += 1
        else:
            counts[low] = 1




highestCount = -1
allMostCommonWords = set()


for low, count in counts.items():
    if count > highestCount:
        allMostCommonWords = {low}
        highestCount = count
    elif count == highestCount:
         allMostCommonWords.add(low)



if len(allMostCommonWords) > 1:
    print ('Is there only one most common word? No.')
    print ('The most common words were', allMostCommonWords,
    'and they occured', highestCount, 'times.')
else:
    print ('Is there only one most common word? Yes.')
    print('The most common word was', "'", allMostCommonWords.pop(), "'",
      'which occurred', highestCount, 'times.')