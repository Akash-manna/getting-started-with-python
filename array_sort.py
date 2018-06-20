#29. Write a Python Program to sort n numbers of data in Ascending order.

a = list()
num = int(input("Enter the Number of elements: "))
print("Enter Array Elements:")

for i in range(int(num)):
    n = int(input("Num {i}: ".format(i = i)))
    a.append(int(n))

print("The Array is:",a)

x = sorted(a)

print("The Sorted Array is: ",x)
