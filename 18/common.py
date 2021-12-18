import re
from math import ceil
from ast import literal_eval

FIRST_NUM = re.compile(r'^([0-9]+).*')
REGULAR_PAIR = re.compile(r'^([0-9]+,[0-9]+).*')


def get_data():
    with open('input.txt') as data:
        return list(map(str.strip, data))


def next_num(string):
    return re.match(FIRST_NUM, string).group(1)


def get_regular_pair(string):
    return re.match(REGULAR_PAIR, string).group(1)


def magnitude(n):
    return _magnitude(literal_eval(n))


def _magnitude(n):
    if isinstance(n, int):
        return n
    else:
        return 3 * _magnitude(n[0]) + 2 * _magnitude(n[1])


def addition(a, b):
    return _reduce(f'[{a},{b}]')


def _reduce(pair):
    while True:
        exploded, pair = explode(pair)
        if exploded:
            continue
        splitted, pair = split(pair)
        if not splitted:
            return pair


def explode(pair):
    level = 0
    last = None
    i = 0
    while i < len(pair):
        c = pair[i]
        if c == '[':
            level += 1
        elif c == ']':
            level -= 1
        elif level == 4 + 1:
            regular_pair = get_regular_pair(pair[i:])
            a, b = (int(n) for n in regular_pair.split(','))
            if last:
                pos, num = last
                pre = pair[:pos] + str(int(num) + a) + pair[pos + len(num): i]
            else:
                pre = pair[:i]
            post = pair[i + len(regular_pair):]
            first = next(((j, next_num(post[j:]))
                         for j, c in enumerate(post) if c.isdigit()),
                         None)
            if first:
                pos, num = first
                post = post[:pos] + str(int(num) + b) + post[pos + len(num):]
            return True, pre[:-1] + '0' + post[1:]
        elif c.isdigit():
            num = next_num(pair[i:])
            last = i, num
            i += len(num) - 1
        i += 1
    return False, pair


def split(pair):
    for i, c in enumerate(pair):
        if c.isdigit():
            num = next_num(pair[i:])
            if (value := int(num)) >= 10:
                return True, (
                    pair[:i] +
                    f'[{value // 2},{ceil(value / 2)}]' +
                    pair[i + len(num):])
    return False, pair
