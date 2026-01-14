#variables
O = 15.9994
C = 12.011
N = 14.00674
S = 32.066
H = 1.00794

num_O = int(input("Number of Oxygen Atoms: "))
num_C = int(input("Number of Carbon Atoms: "))
num_N = int(input("Number of Nitrogen Atoms: "))
num_S = int(input("Number of Sulfur Atoms: "))
num_H = int(input("Number of Hydrogen Atoms: "))

#functions
def molecular_weight():
    result = (O*num_O) + (C*num_C) + (N*num_N) + (S*num_S) + (H*num_H)
    return result

#main
print("The molecular weight of the molecule is: ", molecular_weight(), "g/mol")