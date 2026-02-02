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