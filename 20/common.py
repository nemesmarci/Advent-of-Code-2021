from collections import defaultdict
from itertools import product


class Image():
    def __init__(self):
        self.tiles = defaultdict(lambda: '.')
        with open('input.txt') as data:
            self.lookup = data.readline().strip()
            data.readline()
            for y, line in enumerate(data):
                for x, c in enumerate(line.strip()):
                    self.tiles[(y, x)] = c
        self.min_x = self.min_y = 0
        self.max_x, self.max_y = x, y

    def new_value(self, point):
        ranges = (range(coord - 1, coord + 2) for coord in point)
        bits = ''.join(str(int(self.tiles[(y, x)] == '#'))
                       for y, x in product(*ranges))
        return self.lookup[int(bits, 2)]

    def value(self):
        return sum(1 for y in range(self.min_y, self.max_y + 1)
                   for x in range(self.min_x, self.max_x + 1)
                   if self.tiles[(y, x)] == '#')

    def enhance(self, n):
        new_tiles = defaultdict(lambda: '.' if n % 2 else '#')
        self.min_x -= 1
        self.min_y -= 1
        self.max_x += 1
        self.max_y += 1
        new_tiles.update({(y, x): self.new_value((y, x))
                          for y in range(self.min_y, self.max_y + 1)
                          for x in range(self.min_x, self.max_x + 1)})
        self.tiles = new_tiles

    def iterate(self, n):
        for i in range(n):
            self.enhance(i)
        return self.value()
