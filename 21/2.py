from itertools import product
from collections import Counter, defaultdict

from common import get_starting_tiles, normalize

ROLLS = Counter(map(sum, product([1, 2, 3], repeat=3)))
STATES = defaultdict(lambda: defaultdict(int))


def game(state):
    if state in STATES:
        return STATES[state][0], STATES[state][1]
    first_won = second_won = 0
    t1, t2, p1, p2, player = state
    for score, multiplier in ROLLS.items():
        if player == 1:
            new_tile = normalize(t1 + score)
            if (new_score := p1 + new_tile) >= 21:
                first_won += multiplier
            else:
                fw, sw = game((new_tile, t2, new_score, p2, 2))
                first_won += multiplier * fw
                second_won += multiplier * sw
        else:
            new_tile = normalize(t2 + score)
            if (new_score := p2 + new_tile) >= 21:
                second_won += multiplier
            else:
                fw, sw = game((t1, new_tile, p1, new_score, 1))
                first_won += multiplier * fw
                second_won += multiplier * sw
    STATES[state][0] = first_won
    STATES[state][1] = second_won
    return first_won, second_won


print(max(game((*get_starting_tiles(), 0, 0, 1))))
