from collections import Counter
from itertools import repeat


def get_range(n1, n2):
    return range(n1, n2 + 1) if n1 <= n2 else range(n1, n2 - 1, -1)


def solve(diagonals):
    area = Counter()
    with open('input.txt') as data:
        for line in data:
            (x1, y1), (x2, y2) = ([int(n) for n in x.split(',')]
                                  for x in line.strip().split(' -> '))

            xs = get_range(x1, x2) if diagonals or y1 == y2 else []
            ys = get_range(y1, y2) if diagonals or x1 == x2 else []

            if x1 == x2:
                xs = repeat(x1)
            elif y1 == y2:
                ys = repeat(y1)

            for p in zip(xs, ys):
                area[p] += 1

    return sum(1 for p in area if area[p] > 1)
