#Find the area and circumference of the circle. (Area = pi*r^2; Circumference = 2*pi*r)

r = float(input("Enter the Radius: "))
a= 3.14*r*r
a = round(a,3)
c = 2*3.14*r
c = round(c,3)
print("The Area of the Circle is ",a," and the circumference is ",c)