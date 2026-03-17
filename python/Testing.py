from random import randint

left = 0

current_efficiency = 0
potential_efficiency = 100

def pretend_light():
    global left, current_efficiency, potential_efficiency
    left = randint(0, 30)

def randnum():
    global left, current_efficiency, potential_efficiency
    percentage = ((left + left)/2)*randint(current_efficiency, potential_efficiency)
    return f"Efficiency = {percentage}%"

while True:
    print(randnum())