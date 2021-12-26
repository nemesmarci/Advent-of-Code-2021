east = set()
south = set()

with open('input.txt') as data:
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == '>':
                east.add((y, x))
            elif c == 'v':
                south.add((y, x))

moved = True
i = 0
while moved:
    moved = False
    to_add = set()
    to_remove = set()
    for c in east:
        target = (c[0], c[1] + 1 if c[1] != x else 0)
        if target not in east and target not in south:
            to_add.add(target)
            to_remove.add(c)
            moved = True
    east -= to_remove
    east |= to_add
    to_add = set()
    to_remove = set()
    for c in south:
        target = (c[0] + 1 if c[0] != y else 0, c[1])
        if target not in east and target not in south:
            to_add.add(target)
            to_remove.add(c)
            moved = True
    south -= to_remove
    south |= to_add
    i += 1
print(i)

