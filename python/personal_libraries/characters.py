#import
from typing import Optional

#repeated character printing
def character_printer(amount: int, character: str, new_line_on_end: bool) -> None:
    a=1
    while a<=amount:
        print(f"{character}", end="")
        a=a+1
    if new_line_on_end:
        print()