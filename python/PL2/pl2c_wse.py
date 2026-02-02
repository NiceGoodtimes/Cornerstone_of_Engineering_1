#imports

#variables
column_tracker = 1
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
        pass
    column_tracker += 1