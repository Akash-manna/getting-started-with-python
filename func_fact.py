#20. Write a Python Program using function method to find the factorial of a given Number.

n = int(input("Enter the Number: "))
def fact(n):
    r = 1
    for i in range(1,n+1):
        r = r*i
    return r
fact = fact(n)
print("The Factorial of ",n," is ",fact)
