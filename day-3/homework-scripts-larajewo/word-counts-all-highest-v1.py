#!/usr/bin/env python

#task: Print out all the words with the highest count (there may be many).
 #Hint: use a set to keep track of the most common words. I.e., detect draws.

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


# by now I have I wen trough whole document
# and added all the different words with corresponding counts to the dictionary
# now I want to know if there is one most common word or more and give the corresponding print output


allMostCommonWords = set()

for word, count in counts.items():
    if count == highestCount:
        allMostCommonWords.add(word)


if len(allMostCommonWords) > 1:
    print ('Is there only one most common word? No.')
    print ('The most common words were', allMostCommonWords,
    'and they occured', highestCount, 'times')
else:
    print ('Is there only one most common word? Yes.')
    print ('The most common word was', mostCommonWord,
      'which occurred', highestCount, 'times.')