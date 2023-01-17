#program to find the younger age of the given 2 ages
age1=int(input("enter the first age:"))
age2=int(input("enter the second age:"))
if age1<age2:
    print("first age",age1,"is younger")
elif age2<age1:
    print("second age",age2,"is younger")
else:
    print("both ages",age1,"&",age2,"are equal")
    
