#7. Write a Python Program to read a input from the user and then check whether the given character is an alphabet, number or a special character. If it is an alphabet, convert in to UPPERCASE and vice-versa.

import string
a = input("Enter the String: ")
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
            return False
x = is_number(a)
y = a.isupper()
z = ord(a)
if x:
    print("The String "+a+" is a Number")
else:
    if (z>=0 and z<=47):
        print(a+" is a Special Character!")
    elif (z>=58 and z<=64):
        print(a+" is a Special Character!")
    elif(z>=91 and z<=96):
        print(a+" is a Special Character!")
    elif(z>=123 and z<=126):
        print(a+" is a Special Character!")
    else:
        if y:
            print("The String "+a+"is in UPPERCASE")
            print ("The lowercase is "+a.lower())
        else:
            print("The String is in lowercase")
            print ("The UPPERCASE is "+a.upper())
