#11. Find GCD of two given Numbers.

m = int(input("Enter the First Number: "))
n = int(input("Enter the Second Number: "))
r = m
while(m!=n):
    if(m>n):
        m=m-n
    else:
        n=n-m
print("G.C.D is ",m)
