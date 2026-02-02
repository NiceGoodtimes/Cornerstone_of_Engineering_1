#imports
from python.personal_libraries import is_odd, is_even
#variables
stars = None
spaces = None
#functions
def printer(amount, character):
    a=1
    while a<=amount:
        print(f"{character}", end="")
        a=a+1

#main
for column in range(1,11):
    for row in range(1,5):
        if is_odd(row):
            stars = column
            spaces = 11 - column
            printer(stars, "*")
        elif is_even(row):
            stars = 11-column
            spaces = column
            printer(stars, " ")
