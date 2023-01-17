#program to compute the GCD of two numbers using while loop
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print("The GCD of is:",a)
    
    
    
    
