#program to find the number of digits in a number using recursion
def Count(n):
    if n/10==0:
        return 1
    return 1 + Count(n//10)
n=int(input("Enter a number:"))
print(Count(n)-1)


