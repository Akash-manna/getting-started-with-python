#16. Write a Python Program to print the following pattern
#   0
#   1 0
#   0 1 0

n = int(input("Enter the Number of Rows: "))
for i in range(0, n):
    for j in range(0, i+1):
        print(((i+j)%2), end=" ")
    print("\r")
