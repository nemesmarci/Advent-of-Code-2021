def get_starting_tiles():
    with open('input.txt') as data:
        return [int(line.split(': ')[1]) for line in data]


def normalize(tile):
    return tile if (tile := tile % 10) else 10
