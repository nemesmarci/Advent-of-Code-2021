from collections import defaultdict
from itertools import count


def adjacent(p):
    return ((p[0], p[1] - 1), (p[0], p[1] + 1),
            (p[0] - 1, p[1]), (p[0] + 1, p[1]),
            (p[0] - 1, p[1] - 1), (p[0] + 1, p[1] - 1),
            (p[0] - 1, p[1] + 1), (p[0] + 1, p[1] + 1))


def solve(stop_at_100):
    flashed = 0
    grid = defaultdict(int)

    def process(p):
        nonlocal flashed, to_flash, flashed_this_turn
        grid[p] += 1
        if grid[p] > 9:
            flashed_this_turn.add(p)
            to_flash.add(p)
            grid[p] = 0
            flashed += 1

    with open('input.txt') as data:
        for y, line in enumerate(data):
            for x, o in enumerate(map(int, line.strip())):
                grid[(y, x)] = o
        dimension = y + 1

    for i in count():
        if stop_at_100 and i == 100:
            return flashed

        elif all(grid[(y, x)] == 0
                 for y in range(dimension)
                 for x in range(dimension)):
            return i

        to_flash = set()
        flashed_this_turn = set()
        for p in grid:
            process(p)

        while to_flash:
            p = to_flash.pop()
            for a in adjacent(p):
                if a in grid and a not in flashed_this_turn:
                    process(a)
