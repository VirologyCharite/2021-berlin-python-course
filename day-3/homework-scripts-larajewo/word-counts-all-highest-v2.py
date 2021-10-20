#!/usr/bin/env python

import sys

counts = {}

for line in sys.stdin:
    for word in line.split():
        if word in counts:
            counts[word] = counts[word] + 1 #or counts[low] +=1
        else:
            counts[word] = 1


highestCount = -1
allMostCommonWords = set()


for word, count in counts.items():
    if count > highestCount:
        allMostCommonWords = {word}
        highestCount = count
    elif count == highestCount:
         allMostCommonWords.add(word)



if len(allMostCommonWords) > 1:
    print ('Is there only one most common word? No.')
    print ('The most common words were', allMostCommonWords,
    'and they occured', highestCount, 'times.')
else:
    print ('Is there only one most common word? Yes.')
    print('The most common word was', "'", allMostCommonWords.pop(), "'",
      'which occurred', highestCount, 'times.')
