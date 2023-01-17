#Program to find the fibonacci number using recursin
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter the required element:"))
print(fib(n))



