class Probe():
    def __init__(self, vx, vy):
        self.vx = vx
        self.vy = vy
        self.x = self.y = self.max_y = 0

    def step(self):
        self.x += self.vx
        self.y += self.vy
        if self.y > self.max_y:
            self.max_y = self.y
        if self.vx > 0:
            self.vx -= 1
        self.vy -= 1


def solve():
    with open('input.txt') as data:
        target_x, target_y = (list(map(int, n[2:].split('..')))
                              for n in data.read().strip()[13:].split(', '))
    max_y = 0
    successful = 0
    for try_y in range(target_y[0], target_x[1] + 1):
        for try_x in range(target_x[1] + 1):
            p = Probe(try_x, try_y)
            while p.x <= target_x[1] and p.y >= target_y[0]:
                p.step()
                if p.x in range(target_x[0], target_x[1] + 1) and \
                        p.y in range(target_y[0], target_y[1] + 1):
                    if p.max_y > max_y:
                        max_y = p.max_y
                    successful += 1
                    break
    return max_y, successful
