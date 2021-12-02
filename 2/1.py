from common import solve


def action(instr, value, state):
    if instr == 'forward':
        state.hor += value
    elif instr == 'down':
        state.ver += value
    elif instr == 'up':
        state.ver -= value


print(solve(action))
