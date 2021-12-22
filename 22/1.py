from common import parse

cubes = dict()

for box, action in parse():
    box.x = range(max(box.x[0], -50), min(box.x[-1], 50) + 1)
    box.y = range(max(box.y[0], -50), min(box.y[-1], 50) + 1)
    box.z = range(max(box.z[0], -50), min(box.z[-1], 50) + 1)
    cubes.update({(x, y, z): action == 'on'
                  for x in box.x for y in box.y for z in box.z})

print(sum(cubes.values()))
