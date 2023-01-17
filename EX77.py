#Program to find the harmonic mean of the list of number using function
def harmean(lst):
    sum=0
    for i in lst:
        sum+=1/i
    res = len(lst)/sum
    return str(res)
lst=eval(input("Enter a list:"))
print(harmean(lst))



