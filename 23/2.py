from common import get_data, parse, DOORS, ROOMS, COSTS, solve


def to_room(amphipod, amphipods):
    y, x = amphipod
    type_ = amphipods[amphipod].type
    destx = ROOMS[type_]
    cost = 0
    if (2, destx) not in amphipods and (3, destx) not in amphipods and \
            (4, destx) not in amphipods and (5, destx) not in amphipods:
        desty = 5
        cost = 4
    elif (2, destx) not in amphipods and (3, destx) not in amphipods and \
            (4, destx) not in amphipods and (5, destx) in amphipods and \
            amphipods[(5, destx)].type == type_:
        desty = 4
        cost = 3
    elif (2, destx) not in amphipods and (3, destx) not in amphipods and \
            (4, destx) in amphipods and (5, destx) in amphipods and \
            amphipods[(4, destx)].type == amphipods[(5, destx)].type == type_:
        desty = 3
        cost = 2
    elif (2, destx) not in amphipods and (3, destx) in amphipods and \
        (4, destx) in amphipods and (5, destx) in amphipods and \
            amphipods[(3, destx)].type == amphipods[(4, destx)].type == \
            amphipods[(5, destx)].type == type_:
        desty = 2
        cost = 1
    else:
        return None, None
    if y == 5 and (1, x) not in amphipods and (2, x) not in amphipods and \
            (3, x) not in amphipods and (4, x) not in amphipods:
        cost += 4
    elif y == 4 and (1, x) not in amphipods and (2, x) not in amphipods and \
            (3, x) not in amphipods:
        cost += 3
    elif y == 3 and (1, x) not in amphipods and (2, x) not in amphipods:
        cost += 2
    elif y == 2 and (1, x) not in amphipods:
        cost += 1
    elif y != 1:
        return None, None
    hallway = range(destx, x) if x > destx else range(x + 1, destx + 1)
    if any((1, h) in amphipods for h in hallway):
        return None, None
    return (cost + abs(destx - x)) * COSTS[type_], (desty, destx)


def to_hallway(amphipod, amphipods):
    moves = []
    type_ = amphipods[amphipod].type
    y, x = amphipod
    if y == 5 and (1, x) not in amphipods and (2, x) not in amphipods and \
            (3, x) not in amphipods and (4, x) not in amphipods:
        cost = 4
    elif y == 4 and (1, x) not in amphipods and (2, x) not in amphipods and \
            (3, x) not in amphipods:
        cost = 3
    elif y == 3 and (1, x) not in amphipods and (2, x) not in amphipods:
        cost = 2
    elif y == 2 and (1, x) not in amphipods:
        cost = 1
    else:
        return []
    ranges = (range(x - 1, 0, -1), range(x + 1, 12))
    for range_ in ranges:
        for destx in range_:
            if (1, destx) not in amphipods:
                if (1, destx) not in DOORS:
                    moves.append(((cost + abs(destx - x)) * COSTS[type_],
                                  (1, destx)))
            else:
                break
    return moves


amphipods = get_data((2, 5))
for y, line in zip((3, 4), ("  #D#C#B#A#", "  #D#B#A#C#")):
    amphipods.update(parse(y, line))

print(solve(amphipods, to_room, to_hallway))
