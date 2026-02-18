#imports
from math import cos

#variables
angle = float(input("Enter an angle in radians: "))

#functions
def factorial(x: int) -> int:
    if x <= 1:
        return 1
    else:
        return x * factorial(x-1)

def cosine(x):
    terms = (1,
             -(x**2) / factorial(2),
             +(x**4) / factorial(4),
             -(x**6) / factorial(6),
             +(x**8) / factorial(8))
    return sum(terms)

#main
print(f"Estimated value: {cosine(angle)}")
print(f"Calculated value: {cos(angle)}")
