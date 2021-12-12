from collections import defaultdict


def solve(max_lower):
    area = defaultdict(set)
    with open('input.txt') as data:
        for line in data:
            a, b = line.strip().split('-')
            if b != 'start':
                area[a].add(b)
            if a != 'start':
                area[b].add(a)

    paths = 0
    queue = [('start', ['start'], False)]
    while queue:
        current, visited, twice = queue.pop()
        for n in area[current]:
            if n == 'end':
                paths += 1
            elif n.isupper() or n not in visited or \
                    not twice and visited.count(n) < max_lower:
                p = visited + [n]
                queue.append((n, p, twice or n.islower() and p.count(n) == 2))
    return(paths)
