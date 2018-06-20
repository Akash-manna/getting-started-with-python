#22. Write a Python Program to convert a Binary Numerical to its equivalent Decimal Format.

n = int(input("Enter the Binary Numerical: "))
x = n

def convert(n):
    i = 0
    s = 0
    while (n!=0):
        r = n%10
        s = s+r*pow(2,i)
        i+=1
        n = n//10
    return s

d = convert(n)
print ("The Binary of",x,"is",d)
