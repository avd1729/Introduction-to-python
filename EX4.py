#program to test a number is a prime nuumber
num=int(input("enter a number:"))
lim=int(num/2)+2
for i in range(2,lim):
    rem=num%i
    if rem==0:
        print(num,"is not a prime number")
        break
else:
    print(num,"is a prime number")
