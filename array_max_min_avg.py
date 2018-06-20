#28. Write a Python Program to find the highest, lowest and average from an integer array

a = list()
num = int(input("Enter how many elements you want:"))
print ("Enter numbers in array: ")

for i in range(int(num)):
    n = int(input("num{i}: ".format(i=i)))
    a.append(int(n))
print ("ARRAY: ",a)

max_value = max(a)
min_value = min(a)
avg_value = sum(a)/len(a)

print("Maximum Number is",max_value,"Minimum Number is",min_value,"and the average is",avg_value)
