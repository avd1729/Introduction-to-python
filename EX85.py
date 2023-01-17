#Program to find the maximum number in the list using recursion
def Maximum(lst,l):
    if l==1:
        return lst[0]
    return max(lst[l-1],Maximum(lst,l-1))
lst=eval(input("Enter a list:"))
l=len(lst)
print(Maximum(lst,l))


