#variables
original = str(input("Enter a positive, five-digit number: "))

#functions
def reverser(a):
    return a[::-1]
def square_rooter(a):
    x = float(a)
    return x**0.5
#main
part_1 = f"The square root of {original} is: "
part_3 = f"The square root of {reverser(original)} is: "

print(part_1, square_rooter(original))
print("The number in reverse is:    ", reverser(original))
print(part_3, square_rooter(reverser(original)))