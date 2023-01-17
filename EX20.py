#program to display the length of a number using loop
a=int(input("Enter the number:"))
n=0
while a!=0:
    n+=1
    a=a//10
print("The length of the number is:",n)
