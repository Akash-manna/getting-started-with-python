#27. Write a Python Program to using recusive method to find the GCD of given numbers.

m = int(input("Enter the First Number: "))
n = int(input("Enter the Second Number: "))

def gcd(m,n):
    if(m%n == 0):
        return n
    else:
        return (gcd(n, m%n))

x = gcd(m,n)
print ("GCD is",x)
