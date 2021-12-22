from common import parse, Box


def intersection(box1, box2):
    x = range(max(box1.x[0], box2.x[0]), min(box1.x[-1], box2.x[-1])+1)
    y = range(max(box1.y[0], box2.y[0]), min(box1.y[-1], box2.y[-1])+1)
    z = range(max(box1.z[0], box2.z[0]), min(box1.z[-1], box2.z[-1])+1)
    return Box(x, y, z) if len(x) and len(y) and len(z) else None


def volume(box):
    return (len(box.x)) * (len(box.y)) * (len(box.z))


def split(box, section):
    parts = []
    if box.x[0] < section.x[0]:
        parts.append(
            Box(range(box.x[0], section.x[0]), box.y, box.z))
    if box.x[-1] > section.x[-1]:
        parts.append(
            Box(range(section.x[-1] + 1, box.x[-1] + 1), box.y, box.z))
    if box.y[0] < section.y[0]:
        parts.append(
            Box(section.x, range(box.y[0], section.y[0]), box.z))
    if box.y[-1] > section.y[-1]:
        parts.append(
            Box(section.x, range(section.y[-1] + 1, box.y[-1] + 1), box.z))
    if box.z[0] < section.z[0]:
        parts.append(
            Box(section.x, section.y, range(box.z[0], section.z[0])))
    if box.z[-1] > section.z[-1]:
        parts.append(
            Box(section.x, section.y, range(section.z[-1] + 1, box.z[-1] + 1)))
    return parts


on = set()

for box, action in parse():
    to_remove = set()
    to_add = set()
    for other in on:
        if (section := intersection(box, other)) is not None:
            to_remove.add(other)
            to_add.update(split(other, section))
    on -= to_remove
    on |= to_add
    if action == 'on':
        on.add(box)

print(sum(volume(box) for box in on))
