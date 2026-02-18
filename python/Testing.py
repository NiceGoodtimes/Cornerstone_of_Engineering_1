"""Euler's method
x = 1.0
y = 1.0
dx = 0.1

while x <= 2.5:
    f = x + 3 * y/x
    y = y + f*dx
    x = x +dx
    print(f"x = {x:.3} y = {y:.3}")"""
"""
bala1 = 1.0
bala2 = 2.0
bala3 = 100
bala4 = (bala2-bala1)/bala3
bala5 = bala1**2
bala6 = bala2**2

bala = 0.5*(bala5+bala6)*bala4
for bala0 in range(1,bala3,1):
    bala7 = bala1+bala0*bala4
    bala8 = bala7**2
    bala = bala + bala8*bala4
print(f"Bala's Answer = {bala:.4}")
"""
#def re_lister(value, list_length, n, list_to_add_to):
#    n % list_length
#    list_to_add_to[n] = value
#    return list_to_add_to

"""NOTES:
-replaced time with milliseconds for greater accuracy
"""

from math import exp
print(exp(1))
