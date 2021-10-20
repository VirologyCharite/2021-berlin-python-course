#!/usr/bin/env python

from utils import readInput


def main():
    counts = readInput()
    highestCount = -1
    mostCommonWord = None

    for word, count in counts.items():
        if count > highestCount:
            mostCommonWord = word
            highestCount = count

    print('The most common word was', mostCommonWord,
          'which occurred', highestCount, 'times.')


main()
