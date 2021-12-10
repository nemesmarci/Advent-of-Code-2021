from statistics import median

ILLEGAL = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

INCOMPLETE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

PAIR = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def solve():
    illegal_score = 0
    incomplete_scores = []
    with open('input.txt') as data:
        for line in data:
            illegal = False
            opened = []
            for c in line.strip():
                if opened and c == PAIR[opened[-1]]:
                    opened.pop(-1)
                elif c in PAIR:
                    opened.append(c)
                else:
                    illegal_score += ILLEGAL[c]
                    illegal = True
                    break
            if illegal:
                continue
            incomplete_score = 0
            closers = [PAIR[o] for o in opened[::-1]]
            for c in closers:
                incomplete_score *= 5
                incomplete_score += INCOMPLETE[c]
            incomplete_scores.append(incomplete_score)
    return illegal_score, median(incomplete_scores)
