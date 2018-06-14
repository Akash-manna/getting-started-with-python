#12. Print all Leap Years from a given year to another.

x = int(input("Enter the Starting Year: "))
y = int(input("Enter the Ending Year: "))
print("The Leap Years between ",x," and ",y," are")
for i in range(x,y):
    if(((i%4 == 0) and (i%100!=0)) or (i%400 == 0)):
        print(i)
