from math import prod

from common import get_points, get_lows, get_neighbours


def BFS(start, points):
    queue = [start]
    visited = []
    while queue:
        current = queue.pop(0)

        for p in get_neighbours(current):
            if p not in points or p in visited or points[p] == 9:
                continue
            visited.append(p)
            queue.append(p)

    return len(visited)


lows = get_lows(points := get_points())
sizes = [BFS(low, points) for low in lows]
print(prod(sorted(sizes)[-3:]))
