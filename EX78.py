#Program to find the geometric mean of the list of number using function
import math
def geomean(lst):
    temp=1
    for i in range(0,len(lst)):
        temp = temp * lst[i]
    temp2 = math.pow(temp,(1/len(lst)))
    res=temp2
    return str(res)
lst=eval(input("Enter a list:"))
print(geomean(lst))




