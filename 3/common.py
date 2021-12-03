from collections import Counter, defaultdict


def get_nums():
    with open('input.txt') as data:
        return [line.strip() for line in data]


def get_bits(nums):
    bits = defaultdict(Counter)
    for num in nums:
        for i, bit in enumerate(num):
            bits[i][bit] += 1
    return(bits.values())


def _common(bits, default, index):
    return [default
            if len(mc := bit.most_common()) > 1 and mc[0][1] == mc[1][1]
            else mc[index][0] for bit in bits]


def most_common(bits):
    return _common(bits, '1', 0)


def least_common(bits):
    return _common(bits, '0', -1)


def bits_to_int(bits):
    return int(''.join(bits), 2)
