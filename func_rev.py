#19. Write a Python program in function mehod to reverse any given Number.

n = int(input("Enter the Number to be reversed: "))

def rev(n):
    s = 0
    while(n>0):
        r = n%10
        s = 10*s+r
        n = n//10
    return s

revnum = rev(n)
print("The reverse of ",n," is ",revnum)
