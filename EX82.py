#Program to find the sum of first 'n' numbers using recursion
def Sum(x):
    for i in range(1,x):
        x+=i
    return x
x=int(input("Enter the number of terms:"))
print(Sum(x))


