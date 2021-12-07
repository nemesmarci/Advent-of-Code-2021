from statistics import median

from common import get_data, total_fuel

positions = get_data()
target = int(median(positions))
print(total_fuel(target, positions, linear=True))
