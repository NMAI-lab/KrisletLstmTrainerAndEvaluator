#parses a single line of bayesian.txt e.g. 0.1, 0.2, 0.3
def parse(l):
    l = [float(i) for i in l.split(',')]
    last = len(l) - 1
    return [l[:last], [l[last]]]

with open("bayesian.txt") as f:
    for line in f:
        print(parse(line))


