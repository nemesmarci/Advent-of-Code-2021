from collections import defaultdict

from common import parse


CODE = {
    '0': set('abcefg'),
    '1': set('cf'),
    '2': set('acdeg'),
    '3': set('acdfg'),
    '4': set('bcdf'),
    '5': set('abdfg'),
    '6': set('abdefg'),
    '7': set('acf'),
    '8': set('abcdefg'),
    '9': set('abcdfg')
}


def route(signal, segments):
    return next(correct for correct, mapped in segments.items()
                if signal == list(mapped)[0])


def decode(output, segments):
    return next(
        number for number, signals in CODE.items()
        if set(route(c, segments) for c in output) == signals)


def remove_known(segments, known):
    for segment in segments:
        if segment not in known:
            for signal in known:
                segments[segment] -= segments[signal]


sum_values = 0

with open('input.txt') as data:
    for line in data:
        signals, outputs = parse(line)
        segments = defaultdict(lambda: set('abcdefg'))
        one_missing = set()

        for signal in signals:
            if len(signal) == 2:
                for segment in 'cf':
                    segments[segment] &= set(signal)
            elif len(signal) == 3:
                for segment in 'acf':
                    segments[segment] &= set(signal)
            elif len(signal) == 4:
                for segment in 'bcdf':
                    segments[segment] &= set(signal)
            elif len(signal) == 7:
                for segment in 'abcdefg':
                    segments[segment] &= set(signal)
            elif len(signal) == 6:
                one_missing |= set('abcdefg') - set(signal)

        segments['a'] -= segments['c']
        remove_known(segments, 'a')

        for segment in one_missing:
            if segment in segments['c']:
                segments['c'] = set(segment)
                segments['f'] -= segments['c']
                one_missing -= set(segment)
                break
        remove_known(segments, 'cf')

        for segment in 'de':
            segments[segment] &= one_missing

        common_be = segments['b'] & segments['e']
        segments['b'] -= common_be
        segments['e'] -= common_be
        remove_known(segments, 'bde')

        sum_values += int(''.join(decode(output, segments)
                                  for output in outputs))

print(sum_values)
