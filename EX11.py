#program to calculate the factorial of a number
num=int(input("enter a number:"))
fact=1
a=1
while a<=num:
    fact*=a
    a+=1
print("the factorial of",num,"is",fact)
