from math import prod


def literal(binary, i):
    bits = ''
    while True:
        first = int(binary[i])
        i += 1
        bits += binary[i:i+4]
        i += 4
        if first == 0:
            return int(bits, 2), i


def operator(binary, i, type_id):
    sum_version = 0
    length_type_id = binary[i:i+1]
    i += 1
    sub_packets = []
    if length_type_id == '0':
        sub_len = int(binary[i:i+15], 2)
        i += 15
        sub_i = i + sub_len
        while i < sub_i:
            i, version, sub_value = packet(binary, i)
            sum_version += version
            sub_packets.append(sub_value)
    else:
        sub_num = int(binary[i:i+11], 2)
        i += 11
        for n in range(sub_num):
            i, version, sub_value = packet(binary, i)
            sum_version += version
            sub_packets.append(sub_value)
    if type_id == 0:
        value = sum(sub_packets)
    elif type_id == 1:
        value = prod(sub_packets)
    elif type_id == 2:
        value = min(sub_packets)
    elif type_id == 3:
        value = max(sub_packets)
    elif type_id == 5:
        value = int(sub_packets[0] > sub_packets[1])
    elif type_id == 6:
        value = int(sub_packets[0] < sub_packets[1])
    elif type_id == 7:
        value = int(sub_packets[0] == sub_packets[1])
    return i, sum_version, value


def packet(binary, i):
    version = int(binary[i:i+3], 2)
    i += 3
    type_id = int(binary[i:i+3], 2)
    i += 3
    if type_id == 4:
        value, i = literal(binary, i)
    else:
        i, op_version, value = operator(binary, i, type_id)
        version += op_version
    return i, version, value


def solve():
    with open('input.txt') as data:
        binary = ''
        for c in data.read().strip():
            binary += format(int(c, 16), "04b")
    sum_version = 0
    i = 0
    while i < len(binary) - 8:
        i, version, value = packet(binary, i)
        sum_version += version
    return sum_version, value
