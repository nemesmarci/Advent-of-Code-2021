from common import solve


def action(instr, value, state):
    if instr == 'forward':
        state.hor += value
        state.ver += state.aim * value
    elif instr == 'down':
        state.aim += value
    elif instr == 'up':
        state.aim -= value


print(solve(action))
