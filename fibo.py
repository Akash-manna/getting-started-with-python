#13. Print fibonacci Series (0,1,1,2,3,5,8,...)

n = int(input("Enter the Number of Terms: "))
a = -1
b = 1
print("The Fibonacci Series upto ",n," terms:")
for i in range(0,n):
    c = a +b
    print(c,end=' ')
    a = b
    b = c
