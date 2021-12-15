import math
from queue import PriorityQueue
from collections import defaultdict


def get_data(full):
    area = dict()
    multiplier = 5 if full else 1

    with open('input.txt') as data:
        for y, line in enumerate(map(str.strip, data)):
            dim = len(line)
            for x, risk in enumerate(map(int, line)):
                for off_y in range(multiplier):
                    for off_x in range(multiplier):
                        adjusted = risk + off_x + off_y
                        if adjusted > 9:
                            adjusted -= 9
                        area[(x + off_x * dim, y + off_y * dim)] = adjusted
    return area, dim * multiplier


def get_neighbours(current):
    up = (current[0], current[1] - 1)
    left = (current[0] - 1, current[1])
    right = (current[0] + 1, current[1])
    down = (current[0], current[1] + 1)
    return up, left, right, down


def dijsktra(area, dim):
    start = (0, 0)
    end = (dim - 1, dim - 1)
    risks = defaultdict(lambda: math.inf)
    risks[start] = 0
    visited = set()

    pq = PriorityQueue()
    pq.put((0, start))
    while not pq.empty():
        _, current = pq.get()
        visited.add(current)

        for neighbour in get_neighbours(current):
            if neighbour not in area or neighbour in visited:
                continue
            new_risk = risks[current] + area[neighbour]
            if new_risk < risks[neighbour]:
                pq.put((new_risk, neighbour))
                risks[neighbour] = new_risk
    return risks[end]
