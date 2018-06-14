#14. Print the following Pattern using Python.
#   *
#   **
#   ***
#   ****

n = int(input("Enter the Number of Rows: "))
for i in range(0,(n+1)):
    for j in range(0,i):
        print("*",end='')
    print('')
