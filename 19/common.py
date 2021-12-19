from collections import defaultdict, Counter
from itertools import combinations
from functools import partial


def orientation(vector, o):
    x, y, z = vector
    return \
        (x, y, z) if o == 0 else \
        (x, -z, y) if o == 1 else \
        (x, -y, -z) if o == 2 else \
        (x, z, -y) if o == 3 else \
        (y, -x, z) if o == 4 else \
        (y, -z, -x) if o == 5 else \
        (y, x, -z) if o == 6 else \
        (y, z, x) if o == 7 else \
        (z, y, -x) if o == 8 else \
        (z, x, y) if o == 9 else \
        (z, -y, x) if o == 10 else \
        (z, -x, -y) if o == 11 else \
        (-x, -y, z) if o == 12 else \
        (-x, -z, -y) if o == 13 else \
        (-x, y, -z) if o == 14 else \
        (-x, z, y) if o == 15 else \
        (-y, x, z) if o == 16 else \
        (-y, -z, x) if o == 17 else \
        (-y, -x, -z) if o == 18 else \
        (-y, z, -x) if o == 19 else \
        (-z, x, -y) if o == 20 else \
        (-z, y, x) if o == 21 else \
        (-z, -x, y) if o == 22 else \
        (-z, -y, -x)  # if o == 23


def inverse(vector, o):
    x, y, z = vector
    return \
        (x, y, z) if o == 0 else \
        (x, z, -y) if o == 1 else \
        (x, -y, -z) if o == 2 else \
        (x, -z, y) if o == 3 else \
        (-y, x, z) if o == 4 else \
        (-z, x, -y) if o == 5 else \
        (y, x, -z) if o == 6 else \
        (z, x, y) if o == 7 else \
        (-z, y, x) if o == 8 else \
        (y, z, x) if o == 9 else \
        (z, -y, x) if o == 10 else \
        (-y, -z, x) if o == 11 else \
        (-x, -y, z) if o == 12 else \
        (-x, -z, -y) if o == 13 else \
        (-x, y, -z) if o == 14 else \
        (-x, z, y) if o == 15 else \
        (y, -x, z) if o == 16 else \
        (z, -x, -y) if o == 17 else \
        (-y, -x, -z) if o == 18 else \
        (-z, -x, y) if o == 19 else \
        (y, -z, -x) if o == 20 else \
        (z, y, -x) if o == 21 else \
        (-y, z, -x) if o == 22 else \
        (-z, -y, -x)  # if o == 23


def distance(v1, v2):
    return v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2]


def find_orientation(relative, base, scanners):
    for o in range(23):
        distances = Counter()
        for beacon_b in map(partial(orientation, o=o), scanners[base]):
            for beacon_a in scanners[relative]:
                distances[(distance(beacon_a, beacon_b))] += 1
        mc = distances.most_common(1)
        if mc[0][1] >= 12:
            return o, mc[0][0]


def get_mappings(scanners):
    mapping = defaultdict(dict)
    reverse_mapping = defaultdict(dict)
    for a, b in combinations(scanners, 2):
        offset_details = find_orientation(a, b, scanners)
        if offset_details is not None:
            o, offset = offset_details
            mapping[a][b] = (o, offset)
            reverse_mapping[b][a] = (o, offset)
    return mapping, reverse_mapping


def get_scanners():
    scanners = defaultdict(list)
    with open('input.txt') as data:
        for line in map(str.strip, data):
            if line.startswith('---'):
                scanner = int(line.split()[2])
            elif line:
                scanners[scanner].append(tuple(int(x)
                                               for x in line.split(',')))
    return scanners


def _forward(beacon, o, diff):
    return tuple(x + y for x, y in zip(orientation(beacon, o), diff))


def _backward(beacon, o, diff):
    return inverse((x - y for x, y in zip(beacon, diff)), o)


def rotate(beacon, steps):
    for o, diff, action in steps:
        beacon = action(beacon, o, diff)
    return beacon


def process_base(mapping, i, base, action, actions, scanners):
    o, diff = mapping[i][base]
    actions[i] = [(o, diff, action)] + actions[base]
    scanners[i] = [rotate(beacon, actions[i])
                   for beacon in scanners[i]]


def normalize(scanners, mappings):
    mapping, reverse_mapping = mappings
    actions = defaultdict(list)
    done = set([0])
    while len(done) != len(scanners):
        for i in scanners.keys() - done:
            if not mapping[i] and not reverse_mapping[i]:
                for b in done:
                    offset_details = find_orientation(i, b, scanners)
                    if offset_details is not None:
                        o, offset = offset_details
                        actions[i] = [(o, offset, _backward)]
                        scanners[i] = [rotate(beacon, actions[i])
                                       for beacon in scanners[i]]
                        done.add(i)
                        break
            elif (base := next(filter(
                    lambda x: x in done, mapping[i]), None
                    )) is not None:
                process_base(mapping, i, base, _backward, actions, scanners)
                done.add(i)
            elif (base := next(filter(
                    lambda x: x in done, reverse_mapping[i]), None
                    )) is not None:
                process_base(
                    reverse_mapping, i, base, _forward, actions, scanners)
                done.add(i)
    return actions
