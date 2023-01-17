#program to find the fibonacci series to specified limit
first=0
second=1
num=int(input("enter the number of fibonacci numbers:"))
print(first)
print(second)
for a in range(1,num):
    third=first+second
    print(third)
    first,second=second,third
