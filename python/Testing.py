"""
a^2 + b^2 = c^2
find pythagorean triples
"""
from math import sqrt

def pythagorean(a: int, b: int):
    c = sqrt(a^2 + b^2)

    if c%int(c) != 0.0:
        return 0
    else:
        return int(c)

for i in range(1, 100):
    for j in range(1, 100):
        if pythagorean(i, j) is None:
            continue
        else:
            print(pythagorean(i, j))