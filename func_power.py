#21. Write a Python Program that will take two numbers M and N. Then, it will print M^N.

m = int(input("Enter the Number: "))
n = int(input("Enter the  Power: "))

def power(m,n):
    return m**n
print(n,"th power of",m,"is",power(m,n))
