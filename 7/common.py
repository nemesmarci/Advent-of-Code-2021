def get_data():
    with open('input.txt') as data:
        return list(map(int, data.read().split(',')))


def fuel(position, target, linear):
    distance = abs(position - target)
    return distance if linear else distance * (distance + 1) // 2


def total_fuel(target, positions, linear):
    return sum(fuel(position, target, linear) for position in positions)
