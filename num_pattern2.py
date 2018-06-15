#17. Write a Python Program to print the following pattern
#       1
#      2 3
#     4 5 6
#    7 8 9 10

n = int(input("Enter the Number of Rows: "))
num = 1
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=" ")
    for k in range(1,i+1):
        print(num,end=" ")
        num+=1
    print("\r")
