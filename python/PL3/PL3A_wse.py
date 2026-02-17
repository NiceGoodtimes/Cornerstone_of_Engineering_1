#variables
x = 1.0
y = 1.0
dx = 0.1
f = 0.0

#functions
def first_calculation(independent, dependent):
    part_1 = independent+3
    part_2 = dependent / independent
    result = part_1 * part_2
    return result

def second_calculation(dependent, function_value, interval):
    part_1 = function_value * interval
    result = dependent + part_1
    return result

def third_calculation(independent, interval):
    result = independent + interval
    return result

def result_formatter(first, second):
    result = f"x = {first:.3} y = {second:.3}"
    return result

def combined_function(a, b, c):
    global f
    f = a
    global y
    y = b
    global x
    x = c
    print(result_formatter(x, y))

#main
while x <= 2.5:
    combined_function(first_calculation(x, y),
                      second_calculation(y, f, dx),
                      third_calculation(x, dx))