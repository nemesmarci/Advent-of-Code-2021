class Box():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def parse():
    steps = []
    with open('input.txt') as data:
        for line in map(str.strip, data):
            action, line = line.split()
            x, y, z = line.split(',')
            x = list(map(int, x[2:].split('..')))
            y = list(map(int, y[2:].split('..')))
            z = list(map(int, z[2:].split('..')))
            steps.append([Box(range(x[0], x[1] + 1),
                              range(y[0], y[1] + 1),
                              range(z[0], z[1] + 1)),
                          action])
    return steps
