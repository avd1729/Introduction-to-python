#program to find palindrome of a number
n=int(input("enter number:"))
temp=n
rev=0
while (n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("the number is a paindrome")
else:
    print("the number is not a paindrome")
