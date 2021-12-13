def mirror(c, n):
    return 2 * c - n


def get_data():
    points = set()
    folds = []

    with open('input.txt') as data:
        parsing_points = True
        for line in map(str.strip, data):
            if line == "":
                parsing_points = False
            elif parsing_points:
                x, y = (int(n) for n in line.split(','))
                points.add((x, y))
            else:
                axis, coord = line.split('=')
                folds.append((axis[-1], int(coord)))
    return points, folds


def do_folds(points, folds, stop_at_first):
    for axis, coord in folds:
        to_add = set()
        to_remove = set()

        for p in points:
            x, y = p
            folded = False
            if axis == 'x' and x > coord:
                folded = True
                x = mirror(coord, x)
            elif axis == 'y' and y > coord:
                folded = True
                y = mirror(coord, y)
            if folded:
                to_add.add((x, y))
                to_remove.add(p)

        points -= to_remove
        points |= to_add

        if stop_at_first:
            break
    return points
