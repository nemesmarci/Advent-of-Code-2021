import z3


def solve(fun):
    with open('input.txt') as data:
        params = dict()
        code = data.readlines()
        for i in range(14):
            params[i] = (int(code[i * 18 + 5].split()[-1]),
                         int(code[i * 18 + 15].split()[-1]))
    solver = z3.Optimize()
    digits = z3.IntVector('d', 14)
    model = 0
    z = 0
    for i, d in enumerate(digits):
        solver.add(z3.And(d >= 1, d <= 9))
        a, b = params[i]
        x = z % 26 + a
        if a < 0:
            z /= 26
        z = z3.If(x != d, z * 26 + d + b, z)
        model += d * 10 ** (13 - i)
    solver.add(z == 0)
    getattr(solver, fun)(model)
    solver.check()
    return solver.model().eval(model)
