""" Write a program to input marks of 5 subjects (Physics, Chemistry, English, Maths, Computer Science) for 5 students.
Display rank of each student also result of total marks, percentage, rank in a class. The rank is categorised as fail(mark<40%),
pass & third grade (41% -55%) second grade (56% to 65%), First grade (66% to 75%) Distinction (76% to 90%) and extraordinary (91% to 100%)."""
lst1=[]
lst2=[]
for i in range(0,6):
    Physics_marks=int(input("Enter the Physics marks (out of 100):"))
    Chemistry_marks=int(input("Enter the Chemistry marks (out of 100):"))
    Mathematics_marks=int(input("Enter the Mathematics marks (out of 100):"))
    CSC_marks=int(input("Enter the CSC marks (out of 100):"))
    English_marks=int(input("Enter the English marks (out of 100):"))
    total=(Physics_marks+Chemistry_marks+Mathematics_marks+CSC_marks+English_marks)
    percentage=(total/5)
    lst1.append(total)
    lst2.append(percentage)
    if percentage<40:
        print("GRADE:Fail")
    if percentage>=41 and percentage<=55:
        print("GRADE:Third grade")
    if percentage>=56 and percentage<=65:
        print("GRADE:Second grade")
    if percentage>=66 and percentage<=75:
        print("GRADE:First grade")
    if percentage>=76 and percentage<=90:
        print("GRADE:Distinction")
    if percentage>=91 and percentage<=100:
        print("GRADE:Extraordinary")
    for i in lst1:
        print("totals of the student is:",i)
    for i in lst2:
        print("percentage of the student is:",i)
    
        


    
    



