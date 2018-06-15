#18. Write a program to evaluate the sum of the following series:
#   1+(3/2!)+(5/3!)+...+n

n = int(input("Enter the limit: "))
sum = 0
for i in range(1,n+1):
    fact = 1
    for j in range(1,i):
        sum = sum + ((2*i-1)/fact)
print("The Sum is ",sum)
