#4. If the ages of Mr.X, Mr.Y and Mr.Z are inout through the keyboard, Write a Python program to determine the oldest person among them.

x = int(input("Enter the Age of Mr.X: "))
y = int(input("Enter the Age of Mr.Y: "))
z = int(input("Enter the Age of Mr.Z: "))

if (x>y)and (x>z):
	print("The Oldest Person is Mr.X with Age ",x)
elif (y>x) and (y>z):
	print("The Oldest Person is Mr.Y with Age ",y)
elif (z>x) and (z>y):
	print("The Oldest Person is Mr.Z with Age ",z)
else:
	print("Mr.X, Mr.Y and Mr.Z are of same Age ",x)
