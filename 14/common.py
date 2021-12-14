from collections import Counter


def solve(steps):
    rules = dict()

    with open('input.txt') as data:
        template = list(data.readline().strip())
        data.readline()
        for line in data:
            pair, insert = line.strip().split(' -> ')
            rules[tuple(pair)] = insert
    last = template[-1]

    pairs = Counter()
    for i in range(1, len(template)):
        pair = tuple(template[i-1:i+1])
        pairs[pair] += 1

    for _ in range(steps):
        increment = Counter()
        decrement = Counter()
        for pair in pairs:
            if pair in rules:
                insert = rules[pair]
                n = pairs[pair]
                decrement[pair] += n
                increment[(pair[0], insert)] += n
                increment[(insert, pair[1])] += n
        pairs += increment
        pairs -= decrement

    result = Counter()
    for (p, _), n in pairs.items():
        result[p[0]] += n
    result[last] += 1
    mc = result.most_common()
    return(mc[0][1] - mc[-1][1])
