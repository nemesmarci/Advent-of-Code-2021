from common import get_points, get_lows

points = get_points()
print(sum(points[low] + 1 for low in get_lows(points)))
