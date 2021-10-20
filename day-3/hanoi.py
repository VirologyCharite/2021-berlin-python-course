#!/usr/bin/env python


pegs = [
    [8, 7, 6, 5, 4, 3, 2, 1],
    [],
    [],
]

moves = 0


def drawPegs(move):
    print(f'After move {move}:')
    for pegNumber, peg in enumerate(pegs):
        print('Peg', pegNumber)
        if peg:
            for disc in reversed(peg):
                print('  ', '-' * disc, f'({disc})')
        else:
            print('  empty')

    print()


def move(origin, nDiscs, destination):
    """
    Move all the pegs on the origin peg to the destination peg.
    """
    global moves

    if nDiscs == 1:
        disc = pegs[origin].pop()
        pegs[destination].append(disc)
        moves += 1
    else:
        otherPeg = ({0, 1, 2} - {origin, destination}).pop()

        move(origin, nDiscs - 1, otherPeg)
        move(origin, 1, destination)
        move(otherPeg, nDiscs - 1, destination)

    drawPegs(moves)


drawPegs(0)
move(0, 8, 1)
