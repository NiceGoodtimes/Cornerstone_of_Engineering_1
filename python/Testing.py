x = 1.0
y = 1.0
dx = 0.1

while x <= 2.5:
    f = x + 3 * y/x
    y = y + f*dx
    x = x +dx
    print(f"x = {x:.3} y = {y:.3}")