from common import get_nums, get_bits, bits_to_int, most_common, least_common

bits = get_bits(get_nums())
print(bits_to_int(most_common(bits)) * bits_to_int(least_common(bits)))
