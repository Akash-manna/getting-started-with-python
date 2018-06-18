#26. Write a Python Program using recurssive method to print the fibonacci series.

n = int(input("Enter the number of Items: "))

def fibo(n):
    if((n==0) or (n==1)):
        return n
    else:
        return (fibo(n-1) + fibo(n-2))

print("The Fibonacci series upto",n,"digits is")
for i in range(0,n):
    f = fibo(i)
    print(f,end=' ')
