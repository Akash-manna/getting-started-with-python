#2. Write a Python Program to implement swapping or exchanging two numbers.

first = int(input("Enter the First Number: "))
second = int(input("Enter the Second Number"))
print("Before Swap")
print ("The First Number is ",first," and the Second Number is ",second)
first = first + second
second = first - second
first = first - second
print ("After Swap")
print ("The First Number is ",first," and the Second Number is ",second)
