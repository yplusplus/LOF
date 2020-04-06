import math

def manhattan_dist(p, q):
    return sum([abs(float(x) - float(y)) for x, y in zip(p, q)])

def euclid_dist(p, q):
    return math.sqrt(sum([(float(x) - float(y)) ** 2 for x, y in zip(p, q)]))

def hamming_dist(p, q):
    return sum([0 if x == y else 1 for x, y in zip(p, q)])
