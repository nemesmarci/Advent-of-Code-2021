def parse(line):
    signals, outputs = line.strip().split(' | ')
    return signals.split(), outputs.split()
