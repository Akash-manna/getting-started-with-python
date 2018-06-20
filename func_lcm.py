#23. Write a Python program using function method to find the LCM of given numbers.

a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number:"))
c = int(input("Enter the Third Number: "))

def lcm(a,b):
    x = a
    y = b
    while(a!=b):
        if(a<b):
            a = a+x
        else:
            b = b+y
    return a
d = lcm(a,b)
e = lcm(c,d)
print("The LCM is",e)
