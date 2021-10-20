import sys


def readInput():
    counts = {}

    for line in sys.stdin:
        for word in line.split():
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

    return counts
