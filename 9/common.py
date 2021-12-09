def get_points():
    with open('input.txt') as data:
        return {(x, y): int(height) for y, line in enumerate(data)
                for x, height in enumerate(line.strip())}


def get_neighbours(p):
    return ((p[0], p[1] - 1), (p[0] - 1, p[1]),
            (p[0] + 1, p[1]), (p[0], p[1] + 1))


def get_lows(points):
    return list(filter(lambda p: all(
                           points[n] > points[p] for n in get_neighbours(p)
                           if n in points),
                points))
