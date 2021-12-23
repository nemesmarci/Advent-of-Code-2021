from copy import deepcopy
from queue import PriorityQueue
from functools import total_ordering
from collections import namedtuple


Amphipod = namedtuple('Amphipod', ('type', 'done'))


def parse(y, line):
    return {(y, x): Amphipod(type=c, done=False) for x, c in enumerate(line)
            if c in ('A', 'B', 'C', 'D')}


def get_data(lines):
    amphipods = dict()
    with open('input.txt') as data:
        data.readline()
        data.readline()
        for y, line in zip(lines, data):
            amphipods.update(parse(y, line))
        return amphipods


ROOMS = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
COSTS = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
DOORS = set(((1, 3), (1, 5), (1, 7), (1, 9)))


@total_ordering
class State():
    def __init__(self, cost, state):
        self.cost = cost
        self.state = state

    def __lt__(self, other):
        return (-self.num_done, self.cost) < (-other.num_done, other.cost)

    def __eq__(self, other):
        return self.num_done == other.num_done and self.cost == other.cost

    @property
    def num_done(self):
        return sum(self.state[a].done for a in self.state)


def solve(amphipods, to_room, to_hallway):
    seen = dict()
    states = PriorityQueue()
    states.put(State(0, amphipods))
    finished = set()
    while not states.empty():
        s = states.get()
        cost = s.cost
        state = s.state
        key = frozenset(state.items())
        if key in seen and seen[key] <= cost:
            continue
        else:
            seen[key] = cost

        if finished and min(finished) < cost:
            continue
        for a in state:
            if state[a].done:
                continue
            newcost, loc = to_room(a, state)
            if loc:
                newstate = deepcopy(state)
                type_ = newstate[a].type
                del newstate[a]
                newstate[loc] = Amphipod(type_, done=True)
                if all(newstate[x].done for x in newstate):
                    finished.add(cost + newcost)
                    print('finished', cost + newcost, min(finished))
                else:
                    states.put(State(cost + newcost, newstate))
        for a in state:
            if state[a].done:
                continue
            moves = to_hallway(a, state)
            for newcost, loc in moves:
                newstate = deepcopy(state)
                type_ = newstate[a].type
                del newstate[a]
                newstate[loc] = Amphipod(type_, False)
                states.put(State(cost + newcost, newstate))
    return(min(finished))
