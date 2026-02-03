#setup
from typing import Optional

#even checker
def is_even(n: int) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False

#odd checker
def is_odd(n: int) -> bool:
    if n % 2 == 1:
        return True
    else:
        return False

#distance of tuples
def distance(initial: tuple, final: tuple) -> float:
    dimensions = len(initial)-1
    dimension_sum = 0
    while dimensions >= 0:
        dimension_sum = dimension_sum + (initial[dimensions]**2 - final[dimensions]**2)
        dimensions -= 1
    return dimension_sum**0.5