#8. Check whether a given Number is or not.

n = int(input("Enter the Number: "))
i = 2
flag = 0
while (i<n):
    if (n%i==0):
        flag = 1
        break
    i+=1
if (flag==1):
    print("The Number ",n," is not Prime")
else:
    print("The Number ",n," is Prime")
