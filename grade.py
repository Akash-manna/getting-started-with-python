#Read marks of Physics, Chemistry and Mathematics from the user and calculate average and Grade. Write a  Python Program to print the Grade according to the following Table:
#       Average         Grade
#       >=90            O
#    80<= and >90       A
#    70<= and >80       B
#    60<= and >70       C
#    50<= and >60       D
#       <50            Fail

physics = float(input("Enter the Marks obtained in Physics: "))
chemistry = float(input("Enter the Marks ontained in Chemistry: "))
mathematics = float(input("Enter the Marks obtained in Mathematics: "))
#prcnt = ()((physics+chemistry+mathematics)/300)*100)
avg = ((physics+chemistry+mathematics)/3)
avg = round(avg,2)
if (avg>=90 and avg<=100):
    print ("You are Outstanding. Your Average is ",avg)
elif (avg>=80 and avg<90):
    print ("You are Awesome! Your Average is ",avg)
elif (avg>=70 and avg<80):
    print ("You are The Best! Your Average is ",avg)
elif (avg>=60 and avg<70):
    print ("You are Competitive! Your Average is ",avg)
elif (avg>=50 and avg<60):
    print ("You are A Decision Maker! Your Average is ",avg)
elif (avg<50 and avg>=0):
    print ("Sorry to say that you have to give the Exam again! Your Average is ",avg)
else:
    print ("Please input appropriate Data! Each Marks Should be Between 0 and 100")
