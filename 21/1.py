from common import get_starting_tiles, normalize


def roll(tile, dice, rolled, points):
    for _ in range(3):
        tile += dice
        dice += 1
        if dice > 100:
            dice = 1
    tile = normalize(tile)
    rolled += 3
    points += tile
    return tile, dice, rolled, points


t1, t2 = get_starting_tiles()
dice = 1
rolled = 0
p1 = p2 = 0

while p2 < 1000:
    t1, dice, rolled, p1 = roll(t1, dice, rolled, p1)
    if p1 >= 1000:
        break
    t2, dice, rolled, p2 = roll(t2, dice, rolled, p2)


print(rolled * min(p1, p2))
