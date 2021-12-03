from copy import deepcopy

from common import get_nums, get_bits, bits_to_int, most_common, least_common


def filter_values(values, function):
    i = 0
    while len(values) > 1:
        bits = function(get_bits(values))
        values = list(filter(lambda x: x[i] == bits[i], values))
        i += 1
    return values[0]


print(bits_to_int(filter_values(deepcopy(values := get_nums()), most_common)) *
      bits_to_int(filter_values(values, least_common)))
