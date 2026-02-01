from cmath import inf
from turtledemo.round_dance import stop
import sys
try:
    sys.set_int_max_str_digits(0)
except (AttributeError, ValueError):
    pass


x = int(input("Enter an integer: "))
final=1

if x==0:
    print("Result: 1")
    stop()

while True:
    #print(x)
    final = final*x
    x = abs(x-1)
    if x==1:
        break

str(final)
random_num = final.strip("0")
print(random_num)