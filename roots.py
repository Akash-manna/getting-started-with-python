#Write a Python Program that will calculate teh roots of the quadratic equation with proper error checking of the form
#           ax^2 + bx + c = 0
import math
a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))
c = int(input("Enter the value of C: "))
x1 = int(input("Enter the value of X: "))
x2 = int(input("Enter the value of X2: "))
z = ((b*b)-4*a*c)
d = math.sqrt(z)
if (d>=0):
    x1 = ((-b+d)/(2*a))
    x2 = ((b-d)/(2*a))
    print("The value of real root area is ",x1, " to ",x2)
else:
    print("No Real Root")
