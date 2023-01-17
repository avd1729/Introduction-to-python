#Program to find all possible permutations of the given string
def toString(lst):
    return ''.join(lst)
def permute(a,l,r):
    if l==r:
        print(toString(a))
    else:
        for i in range(l,r+1):
            a[1],a[i] = a[i],a[1]
            permute(a,l+1,r)
            a[l],a[i] = a[i],a[1]
st=input('Enter a string:')
n=len(st)
a=list(st)
permute(a,0,n-1)
