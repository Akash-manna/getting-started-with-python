#25. Write a Python Program using recurssive method to reverse any given Number.

n = int(input("Enter the Number: "))

def reverse(n):
   if n<10:
      return n
   else:
      return int(str(n%10) + str(reverse(n//10)))

x = reverse(n)
print("The reverse is",x)
