from math import exp
#variables
a = 1
b = 2
n = int(input("Enter the number of subintervals: "))
subint_width = (b-a) / n
current_n = a + subint_width
heights = 0

#functions
def f(x):
    return exp(1)**(-(x**2))

def trapez(lower_bound, upper_bound, delta_x):
    global current_n
    global heights
    #calculates function height for each subinterval
    heights = f(lower_bound) + f(upper_bound)
    while current_n != upper_bound:
        heights = heights + 2 * f(current_n)
        current_n += delta_x
    #calculates the area based on function heights
    area = 0.5*delta_x*heights
    return area

#main
print(f"Area: {trapez(a, b, subint_width)}")