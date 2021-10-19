import sys

namesWeHaveSeenSoFar = set()

for line in sys.stdin:
    line = line.rstrip()
    if line.startswith('>'):
        name = line[1:]
        if name in namesWeHaveSeenSoFar:
            print("Holy shit, we've already seen", name)
        else:
            namesWeHaveSeenSoFar.add(name)
        # print(name)
