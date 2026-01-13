#Variables
x1 = float(input("X of point 1: "))
y1 = float(input("Y of point 1: "))

x2 = float(input("X of point 2: "))
y2 = float(input("Y of point 2: "))

#functions
def slope_calculator():
    m = (y2 - y1) / (x2 - x1)
    return m

def final_answer():
    if x1 == x2 and y1 == y2:
        return "the lines form a point"
    else:
        return "error"

#main