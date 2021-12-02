class State:
    hor = 0
    ver = 0
    aim = 0


def solve(action):
    state = State()
    with open('input.txt') as data:
        for line in data:
            instr, value = line.strip().split()
            action(instr, int(value), state)
    return(state.hor * state.ver)
