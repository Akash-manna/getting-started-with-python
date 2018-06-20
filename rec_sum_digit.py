#24. Write a Python Program using recursive method to find the sum of digits of a Number.

n = int(input("Enter the Number: "))

def sumd(n):
    """ Return the sum of digits of a number.
        number: non-negative integer
    """

    # Base Case
    if n == 0:
        return 0
    else:
        # Mod (%) by 10 gives you the rightmost digit (227 % 10 == 7),
        # while doing integer division by 10 removes the rightmost
        # digit (227 // 10 is 22)

        return (n % 10) + sumd(n // 10)

x = sumd(n)
print ("Sum of digits is ",x)
