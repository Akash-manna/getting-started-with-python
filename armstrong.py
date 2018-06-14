#10. Check whether a given Number is Armstrong or not

n = int(input("Enter the Number: "))
m = n
s = 0
while (n>0):
    r = n%10
    n = n//10
    s = (s+(r*r*r))
if(s==m):
    print("The Number ",m," is Armstrong Number!")
else:
    print("The Number is not a Armstrong Number!")

"""
num = int(input("enter a number: "))
length = len(str(num))
sum = 0
temp = num
while(temp != 0):
    sum = sum + ((temp % 10) ** length)
    temp = temp // 10
if sum == num:
    print("armstrong number")
else:
    print("not armstrong number")
"""
