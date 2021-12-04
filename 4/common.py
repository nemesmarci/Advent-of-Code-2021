def read_data():
    tables = {}
    with open('input.txt') as data:
        numbers = tuple(map(int, data.readline().split(',')))
        i = 0
        while data.readline():
            tables[i] = [list(map(int, data.readline().split()))
                         for j in range(5)]
            i += 1
    return numbers, tables


def is_winner(table):
    return any(not any(row) for row in table) or \
           any(not any(row[i] for row in table) for i in range(5))


def find_winner(numbers, tables, return_first):
    tables_in_game = set(tables.keys())
    for wnumber in numbers:
        eliminated = set()
        if len(tables_in_game) == 1:
            return_first = True
        for i in tables_in_game:
            for row in tables[i]:
                if wnumber in row:
                    row[row.index(wnumber)] = None
                    if is_winner(tables[i]):
                        if return_first:
                            return wnumber, tables[i]
                        eliminated.add(i)
                    break
        for d in eliminated:
            del tables[d]
        tables_in_game -= eliminated


def table_score(table):
    return sum(sum(filter(None, row)) for row in table)


def solve(first):
    wnumber, winner = find_winner(*read_data(), first)
    return(table_score(winner) * wnumber)
