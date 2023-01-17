#program to find the factorial of a number using functions
def fact(n):
    if n==0 or n==1:
        ans=1
    elif n>1:
        ans=n*fact(n-1)
    else:
        ans="/Invalid"
    return ans
n=int(input("Enter a number:"))
print(fact(n))



