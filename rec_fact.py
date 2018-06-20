#26. Write a Python Program using recurssive method to find the factorial of a given number.

n = int(input("Enter the Number: "))
x = n

def fact(n):
    if n==0:
        return 1
    else:
        return (n*fact(n-1))

x = fact(n)
print("The Factorial of",n,"is",x)
