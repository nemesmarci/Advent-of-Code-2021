from itertools import combinations
from common import get_scanners, get_mappings, normalize, rotate


def manhattan(v1, v2):
    return abs(v1[0] - v2[0]) + abs(v1[1] - v2[1]) + abs(v1[2] - v2[2])


steps = normalize(scanners := get_scanners(), get_mappings(scanners))
locations = [rotate((0, 0, 0), steps[i]) for i in scanners]

print(max(manhattan(locations[a], locations[b])
          for a, b in combinations(scanners, 2)))
