#9. Write a Python Program to make the Sum of a given digit

n = int(input("Enter the Number: "))
r = n
sum = 0
while (n>0):
    r = n%10
    n = n//10
    sum = sum + r
print("The Sum of the digits is",sum)
