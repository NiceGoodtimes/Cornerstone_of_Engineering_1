#variables
increment = int(input("Enter the increment for the conversion table in Fahrenheit: "))
f_row = 0

#functions
def f_to_k(fahrenheit):
    kelvin = ((5/9)*(fahrenheit-32))+273.15
    return int(kelvin)

#table creator
print("Fahrenheit     Kelvin")
while f_row <= 200:
    print(f_row, "     ", f_to_k(f_row))
    f_row = f_row + increment