from statistics import median

from common import get_data, total_fuel

positions = get_data()
target = int(median(positions))
min_consumption = total_fuel(target, positions, linear=False)
left = right = True
while True:
    if left and \
            (consumption := total_fuel(target - 1, positions, linear=False)) \
            < min_consumption:
        target -= 1
        min_consumption = consumption
        right = False
    elif right and \
            (consumption := total_fuel(target + 1, positions, linear=False)) \
            < min_consumption:
        target += 1
        min_consumption = consumption
        left = False
    else:
        print(min_consumption)
        break
