from collections import Counter, deque


def solve(days):
    with open('input.txt') as data:
        fish = Counter(map(int, data.read().split(',')))
        fish = deque(fish[i] for i in range(9))

    for i in range(days):
        new = fish[0]
        fish.rotate(-1)
        fish[6] += new
        fish[8] = new

    return(sum(fish))
