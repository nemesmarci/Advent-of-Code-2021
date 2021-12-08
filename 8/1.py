from common import parse

easy = 0

with open('input.txt') as data:
    print(sum(len(output) in (2, 3, 4, 7)
              for line in data for output in parse(line)[1]))
