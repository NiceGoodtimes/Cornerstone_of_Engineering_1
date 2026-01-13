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
        print("Alert: the points do not form a line")
    elif x1 == x2:
        print("Alert: the points form a vertical line\nSlope: Infinite")
    elif y1 == y2:
        print("Alert: the points form a horizontal line\nSlope: 0")
    else:
        print("slope: ", slope_calculator())
    return 0

#main SECTION
final_answer()